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
from dataclasses import dataclass

import numpy as np
import pandas as pd
import re
from .. import utils
from ..maker_settings import MakerSettings


@dataclass
class FourierModel:
    n_coeffs: int
    min_period: str
    max_period: str
    period_spacing: str


def generate_fourier(settings: MakerSettings, model: FourierModel):
    """Generates a Fourier-based series with a catalog and metadata."""
    min_period_sec = _parse_period_to_seconds(model.min_period)
    max_period_sec = _parse_period_to_seconds(model.max_period)

    if model.period_spacing == "linear":
        periods = np.linspace(min_period_sec, max_period_sec, model.n_coeffs)
    else:
        periods = np.geomspace(min_period_sec, max_period_sec, model.n_coeffs)

    coeffs = np.random.uniform(-1, 1, model.n_coeffs)
    chunk_time = np.arange(0, max_period_sec, settings.time_step)
    chunk_signal = np.sum(
        c * np.sin(2 * np.pi * (1 / p) * chunk_time)
        for c, p in zip(coeffs, periods)
        if p > 0
    )

    timestamps = utils.generate_timestamps(settings)
    n_samples = len(timestamps)
    indices = (
        np.arange(n_samples) % np.size(chunk_signal)
        if len(chunk_signal) > 0
        else np.zeros(n_samples, dtype=int)
    )
    values = chunk_signal[indices]

    metric_id = 1001

    data_df = pd.DataFrame(
        {"metric_id": metric_id, "timestamp": timestamps, "value": values}
    )

    catalog_df = pd.DataFrame(
        [
            {
                "metric_id": metric_id,
                "name": "fourier_signal",
                "tags": {
                    "generator": "fourier",
                    "n_coeffs": model.n_coeffs,
                    "spacing": model.period_spacing,
                },
            }
        ]
    )

    metadata = {"coefficients": coeffs.tolist(), "periods_sec": periods.tolist()}

    return data_df, catalog_df, metadata


def _parse_period_to_seconds(period_str):
    """Converts a period string like '1d', '3h', '30m', '10s' to seconds."""
    match = re.match(r"(\d+)([dhms])", period_str.lower())
    if not match:
        raise ValueError(
            f"Invalid period format: {period_str}. Use 'd', 'h', 'm', or 's'."
        )
    value, unit = match.groups()
    return int(value) * {"d": 86400, "h": 3600, "m": 60, "s": 1}[unit]
