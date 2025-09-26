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

import pyarrow as pa
import pyarrow.dataset as ds


class ArrowDataSetPersistence(Persistence):
    def read(self, path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        base_path = Path(path)

        if not base_path.exists():
            raise ValueError(f"Cannot find location {base_path}.")
        if base_path.is_file():
            raise ValueError("Cannot read Arrow DataSet from file.")

        data_path = base_path / "data"
        catalog_path = base_path / "catalog"

        data_dataset = ds.dataset(data_path, format="parquet")
        catalog_dataset = ds.dataset(catalog_path, format="parquet")
        return (
            data_dataset.to_table().to_pandas(),
            catalog_dataset.to_table().to_pandas(),
        )

    def write(self, path: str, data_df: pd.DataFrame, catalog_df: pd.DataFrame):
        base_path = Path(path)

        if base_path.is_file():
            raise ValueError("Cannot write Arrow DataSet to file.")
        base_path.mkdir(parents=True, exist_ok=True)

        data_path = base_path / "data"
        catalog_path = base_path / "catalog"

        data_path.mkdir(parents=True, exist_ok=True)
        catalog_path.mkdir(parents=True, exist_ok=True)

        data_table = pa.Table.from_pandas(data_df)
        ds.write_dataset(data_table, data_path, format="parquet", partitioning=None)

        catalog_table = pa.Table.from_pandas(catalog_df)
        ds.write_dataset(
            catalog_table, catalog_path, format="parquet", partitioning=None
        )
