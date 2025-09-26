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
from deltalake import DeltaTable, write_deltalake

from tsmaker.persistence import Persistence


class DeltaLakePersistence(Persistence):
    def read(self, requested_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        base_path = Path(requested_path)

        if not base_path.exists():
            raise ValueError(
                f"Cannot read DeltaLake from {base_path}, because it does not exist"
            )
        if base_path.is_file():
            raise ValueError(f"Cannot read DeltaLake from a file {base_path}")

        data_df = DeltaTable(base_path / "data").to_pandas()
        if "timestamp" in data_df.columns:
            data_df["timestamp"] = data_df["timestamp"].astype("datetime64[ns]")

        catalog_df = DeltaTable(base_path / "catalog").to_pandas()

        return data_df, catalog_df

    def write(
        self, requested_path: str, data_df: pd.DataFrame, catalog_df: pd.DataFrame
    ):
        base_path = Path(requested_path)

        if base_path.is_file():
            raise ValueError("Cannot write DeltaLake format to a file.")

        if not base_path.exists():
            base_path.mkdir()

        data_path = base_path / "data"
        catalog_path = base_path / "catalog"

        data_path.mkdir(exist_ok=True)
        catalog_path.mkdir(exist_ok=True)

        write_deltalake(data_path, data_df, mode="overwrite")
        write_deltalake(catalog_path, catalog_df, mode="overwrite")
