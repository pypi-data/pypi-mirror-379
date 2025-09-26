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
from typing import Dict, Any, Tuple

import pandas as pd

from tsmaker.persistence.arrow_data_set import ArrowDataSetPersistence
from tsmaker.persistence.csv import CSVPersistence
from tsmaker.persistence.delta_lake import DeltaLakePersistence
from tsmaker.persistence.iceberg import IcebergPersistence
from tsmaker.persistence.influx import InfluxPersistence
from tsmaker.persistence.parquet import ParquetPersistence
from tsmaker.persistence.tsv import TSVPersistence

FILE_FORMAT_MAP = {
    "csv": CSVPersistence,
    "tsv": TSVPersistence,
    "parquet": ParquetPersistence,
    "arrow": ArrowDataSetPersistence,
    "delta": DeltaLakePersistence,
    "iceberg": IcebergPersistence,
    "influx": InfluxPersistence,
}


def save_time_series(
    data_df: pd.DataFrame,
    catalog_df: pd.DataFrame,
    metadata: Dict[str, Any],
    base_path: str,
    file_format: str,
):
    """
    Saves all generated outputs (DataFrames and metadata) to disk.

    Args:
        data_df (pd.DataFrame): Time series data
        catalog_df (pd.DataFrame): Catalog data
        metadata (dict): The metadata dictionary to save.
        base_path (str): The base output path provided by the user.
        file_format (str): The desired output format (e.g., 'csv', 'parquet').
    """
    persistence_class = FILE_FORMAT_MAP[file_format]
    persistence = persistence_class()

    # Saving time series data and catalog
    persistence.write(base_path, data_df, catalog_df)

    # Save metadata if it exists
    metadata_path = f"{base_path}/metadata.json"
    print(f"Writing metadata to {metadata_path}...")
    if metadata:
        persistence.write_metadata(metadata_path, metadata)
    else:
        print("No metadata to save.")
    print("...Done.")


def read_time_series(
    path: str, file_format: str
) -> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, Any]]:
    """
    Reads time series data and metadata from disk.

    :param path: Path where the find the files
    :param file_format: File format that was used to write
    :return: Data DataFrame, Catalog DataFrame, Metadata dictionary
    """
    base_path = Path(path)

    if not base_path.exists():
        raise ValueError("The specified path does not exist.")
    if not base_path.is_dir():
        raise ValueError("The specified path is not a directory.")

    persistence_class = FILE_FORMAT_MAP[file_format]
    persistence = persistence_class()
    # Read time series data and catalog
    data_df, catalog_df = persistence.read(path)

    # Read metadata if it exists
    metadata_path = base_path / "metadata.json"
    metadata = {}
    if Path(metadata_path).exists():
        metadata = persistence.read_metadata(str(metadata_path))

    return data_df, catalog_df, metadata
