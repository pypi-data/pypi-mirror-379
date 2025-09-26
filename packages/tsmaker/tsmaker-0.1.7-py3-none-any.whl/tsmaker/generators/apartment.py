# Copyright (C) 2025 Joris Gillis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import datetime
import pandas as pd
import numpy as np
import itertools
from .. import utils
from ..maker_settings import MakerSettings


#################################################################################
## Modeling the apartment
#################################################################################
class BaseModel:
    def get_context(self, date, existing_context):
        raise NotImplementedError


class SeasonalModel(BaseModel):
    def get_context(self, date, existing_context):
        month = date.month
        if month in [6, 7, 8]:
            base_temp, sunrise_hour, sunset_hour = 21.0, 6, 21
        elif month in [12, 1, 2]:
            base_temp, sunrise_hour, sunset_hour = 16.0, 8, 17
        else:
            base_temp, sunrise_hour, sunset_hour = 18.0, 7, 19
        return {
            "base_temp_c": base_temp,
            "sunrise": datetime.time(hour=sunrise_hour),
            "sunset": datetime.time(hour=sunset_hour),
        }


class DayTypeModel(BaseModel):
    def get_context(self, date, existing_context):
        return {"is_weekend": date.weekday() >= 5}


class WeatherModel(BaseModel):
    def get_context(self, date, existing_context):
        return {"cloudiness": np.random.uniform(0.1, 0.9)}


class OccupancyProfileModel(BaseModel):
    def get_context(self, date, existing_context):
        is_weekend = existing_context.get("is_weekend", False)
        if is_weekend:
            profile = {(0, 8): 0.95, (8, 23): 0.8}
        else:
            profile = {(0, 7): 0.95, (7, 9): 0.5, (9, 17): 0.1, (17, 23): 0.9}
        return {"occupancy_profile": profile}


class DailyContext:
    def __init__(self, current_date):
        self.date = current_date
        self.context = {}
        self.models = [
            SeasonalModel(),
            DayTypeModel(),
            WeatherModel(),
            OccupancyProfileModel(),
        ]
        self._run_models()

    def _run_models(self):
        for model in self.models:
            new_params = model.get_context(self.date, self.context)
            if any(key in self.context for key in new_params):
                raise ValueError(f"Key collision in {model.__class__.__name__}")
            self.context.update(new_params)


def _calculate_occupancy(ts, context):
    hour = ts.hour
    for time_range, prob in context["occupancy_profile"].items():
        if time_range[0] <= hour < time_range[1]:
            return np.random.rand() < prob
    return False


def _calculate_ambient_light(ts, context):
    return (
        1.0 - (0.9 * context["cloudiness"])
        if context["sunrise"] <= ts.time() < context["sunset"]
        else 0.0
    )


#################################################################################
## Generating time series for the apartment
#################################################################################
def generate_apartment_sensors(settings: MakerSettings):
    """Generates coupled apartment sensor data with a catalog."""

    # 1. Define the catalog for all sensors
    sensors = ["temperature", "humidity", "co2_ppm", "light_lux", "motion"]
    metric_id_counter = itertools.count(1001)
    catalog_records = [
        {
            "metric_id": next(metric_id_counter),
            "name": sensor,
            "tags": {"generator": "apartment", "sensor_type": sensor},
        }
        for sensor in sensors
    ]
    catalog_df = pd.DataFrame(catalog_records)
    sensor_to_id = {rec["name"]: rec["metric_id"] for rec in catalog_records}

    # 2. Run simulation
    data_records = []
    current_day_iterator = settings.start_date.date()
    while current_day_iterator <= settings.end_date.date():
        daily_context = DailyContext(current_day_iterator).context
        day_start = datetime.datetime.combine(current_day_iterator, datetime.time.min)
        day_end = datetime.datetime.combine(current_day_iterator, datetime.time.max)
        timestamps = [
            ts
            for ts in utils.generate_timestamps(
                MakerSettings(day_start, day_end, settings.time_step, settings.jitter)
            )
            if ts <= settings.end_date
        ]

        for ts in timestamps:
            occupancy = _calculate_occupancy(ts, daily_context)
            ambient_light = _calculate_ambient_light(ts, daily_context)

            values = {
                "temperature": np.clip(
                    daily_context["base_temp_c"]
                    + (ambient_light * 2.0)
                    + (1.0 if occupancy else 0.0)
                    + np.random.normal(0, 0.2),
                    10,
                    40,
                ),
                "humidity": np.clip(
                    45.0 + (10.0 if occupancy else 0.0) + np.random.normal(0, 2.0),
                    10,
                    90,
                ),
                "co2_ppm": np.clip(
                    400
                    + (
                        np.random.uniform(200, 800)
                        if occupancy
                        else np.random.uniform(5, 50)
                    ),
                    400,
                    2000,
                ),
                "light_lux": np.clip(
                    (ambient_light * 500)
                    + (
                        300
                        if occupancy and ambient_light < 0.2
                        else np.random.uniform(10, 100)
                    )
                    + np.random.normal(0, 5),
                    0,
                    1000,
                ),
                "motion": 1 if occupancy and np.random.rand() < 0.1 else 0,
            }

            for sensor, value in values.items():
                data_records.append(
                    {"metric_id": sensor_to_id[sensor], "timestamp": ts, "value": value}
                )

        current_day_iterator += datetime.timedelta(days=1)

    data_df = pd.DataFrame(data_records)
    return data_df, catalog_df, {}
