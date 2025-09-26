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
from typing import Tuple, Callable

import pandas as pd

from tsmaker.persistence import Persistence


class FilePersistence(Persistence):
    def __init__(
        self,
        write_function: Callable[[str, pd.DataFrame], None],
        read_function: Callable[[str], pd.DataFrame],
        file_extension: str,
    ):
        self._write_function = write_function
        self._read_function = read_function
        self._file_extension = file_extension

    def read(self, path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        base_path = Path(path)

        if base_path.is_file():
            raise ValueError("Cannot read from a single file")

        if not base_path.exists():
            raise ValueError(f"Location cannot be found: {base_path}")

        data_df = self._read_function(str(base_path / f"data.{self._file_extension}"))
        data_df["timestamp"] = data_df["timestamp"].astype("datetime64[ns]")
        catalog_df = self._read_function(
            str(base_path / f"catalog.{self._file_extension}")
        )

        return (
            data_df,
            catalog_df,
        )

    def write(self, path: str, data_df: pd.DataFrame, catalog_df: pd.DataFrame):
        base_path = Path(path)

        if base_path.is_file():
            raise ValueError(f"Cannot write Parquet to a file: {base_path}")
        base_path.mkdir(parents=True, exist_ok=True)

        data_path = base_path / f"data.{self._file_extension}"
        catalog_path = base_path / f"catalog.{self._file_extension}"

        self._write_function(str(data_path), data_df)
        self._write_function(str(catalog_path), catalog_df)
