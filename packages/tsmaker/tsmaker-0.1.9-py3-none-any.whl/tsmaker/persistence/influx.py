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
from pathlib import Path
from typing import Tuple
import pandas as pd

from tsmaker.persistence import Persistence


class InfluxPersistence(Persistence):
    def read(self, path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Reads a file in InfluxDB line protocol format and returns two DataFrames.

        The file is expected to contain lines formatted as the InfluxDB line protocol, with the following elements:
        - measurement: String that identifies the measurement to store the data in.
        - tag set: Comma-delimited list of key-value pairs, each representing a tag.
        - field set: Comma-delimited list of key-value pairs, each representing a field.
        - timestamp: Unix timestamp associated with the data.

        The function returns two DataFrames:
        - data_df: Contains the time series data with columns: metric_id, timestamp, value.
        - catalog_df: Contains the catalog data with columns: metric_id, name, tags.

        :param path: Path to the file to read.
        :return: A tuple of two DataFrames (data_df, catalog_df).
        """
        data = []
        catalog = []

        with open(Path(path) / "data.influx", "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Split the line into components
            parts = line.split(" ")
            measurement = parts[0].split(",")[0]
            tag_set = parts[0].split(",")[1:]
            field_set = parts[1]
            timestamp = parts[2]

            # Parse the tag set
            tags = {}
            for tag in tag_set:
                key, value = tag.split("=")
                tags[key] = value

            # Parse the field set
            field_key, field_value = field_set.split("=")
            value = float(field_value)

            if "metric_id" in tags.keys():
                metric_id = tags["metric_id"]
                del tags["metric_id"]
            else:
                # Create a unique metric_id for each measurement and tag set combination
                metric_id = (
                    f"{measurement}_{'_'.join([f'{k}={v}' for k, v in tags.items()])}"
                )

            # Append to data and catalog
            data.append(
                {
                    "metric_id": metric_id,
                    "timestamp": pd.to_datetime(int(timestamp), unit="ns"),
                    "value": value,
                }
            )

            catalog.append({"metric_id": metric_id, "name": measurement, "tags": tags})

        data_df = pd.DataFrame(data, columns=["metric_id", "timestamp", "value"])
        data_df["timestamp"] = data_df["timestamp"].astype("datetime64[us]")
        catalog_df = pd.DataFrame(catalog)

        return data_df, catalog_df

    def write(self, path: str, data_df: pd.DataFrame, catalog_df: pd.DataFrame):
        """
        Writes a DataFrame to the InfluxDB line protocol.

        Given two dataframes with the following columns:
        - data_df: metric_id, timestamp, value
        - catalog_df: metric_id, name, tags

        Dataframe data_df contains the time series data. The metric_id column is used to link the data with the metadata
        in Dataframe catalog_df. The Dataframe catalog_df contains the metric_id for linking, the name (called
        measurement in InfluxDB line protocol) and the tags (tag set in InfluxDB line protocol).

        Each row of the Dataframe data_df is converted in a single line in the output file. The line is formatted as the
        InfluxDB line protocol (more info later). Each row of the data_df Dataframe needs to be joined to the corresponding
        row in the Dataframe catalog_df, using the metric_id as the join column. This join contains all the information to
        write out the line in the InfluxDB line protocol.

        In InfluxDB, a point contains a measurement name (= name from catalog_df), one or more fields (= value from the
        time series), a timestamp, and optional tags (= key-value pair from catalog_df) that provide metadata about the
        observation.

        Each line of line protocol contains the following elements:

        **Required elements**

            - *measurement*: String that identifies the measurement to store the data in.

            - *field set*: Comma-delimited list of key value pairs, each representing a field. Field keys are unquoted
            strings. Spaces and commas must be escaped. Field values can be strings ( quoted), floats, integers,
            unsigned integers, or booleans.

        **Optional elements**

            - *tag set*: Comma-delimited list of key value pairs, each representing a tag. Tag keys and values are
            unquoted strings. Spaces, commas, and equal characters must be escaped.

            - *timestamp*: Unix timestamp associated with the data. InfluxDB supports up to nanosecond precision. If the
            precision of the timestamp is not in nanoseconds, you must specify the precision when writing the data to
            InfluxDB.

        For this function, all elements are required. The order of the fields is:

            1. measurements
            2. tag set
            3. field set
            4. timestamp

        :param path: Path to write the data to
        :param data_df: Dataframe with the time series data
        :param catalog_df: Dataframe with the catalog data
        """
        # Merge data_df and catalog_df on metric_id
        merged_df = pd.merge(data_df, catalog_df, on="metric_id")

        # Prepare the lines for the InfluxDB line protocol
        lines = []
        for _, row in merged_df.iterrows():
            measurement = row["name"]
            tags = row["tags"]
            value = row["value"]
            timestamp = row["timestamp"].value

            # Format the tags
            metric_id_value = f"metric_id={row['metric_id']}"
            key_value_tags = [metric_id_value] + [f"{k}={v}" for k, v in tags.items()]
            tag_set = ",".join(key_value_tags)

            # Format the line
            line = f"{measurement},{tag_set} value={value} {timestamp}"
            lines.append(line)

        # Write the lines to the file
        base_path = Path(path)
        base_path.mkdir(parents=True, exist_ok=True)
        file_path = base_path / "data.influx"

        with open(file_path, "w") as f:
            f.write("\n".join(lines))
