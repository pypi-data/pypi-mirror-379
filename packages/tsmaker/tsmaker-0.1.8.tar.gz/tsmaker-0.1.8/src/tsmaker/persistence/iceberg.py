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
import pyarrow as pa
from pyiceberg.catalog import load_catalog

from tsmaker.persistence import Persistence


class IcebergPersistence(Persistence):
    SQLITE_CATALOG_FILE_NAME = "pyiceberg_catalog.db"

    DEFAULT_NAMESPACE = "default"
    DATA_TABLE_ID = f"{DEFAULT_NAMESPACE}.data"
    CATALOG_TABLE_ID = f"{DEFAULT_NAMESPACE}.catalog"

    def read(self, path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        base_path = Path(path)

        if not base_path.exists():
            raise ValueError(
                f"Could not find path for Iceberg persistence: {base_path}"
            )
        if base_path.is_file():
            raise ValueError("Iceberg can only be read from a directory")

        catalog = load_catalog(
            self.DEFAULT_NAMESPACE,
            **{
                "type": "sql",
                "uri": f"sqlite:///{base_path / self.SQLITE_CATALOG_FILE_NAME}",
                "warehouse": f"file://{base_path}",
            },
        )
        data_table = catalog.load_table(self.DATA_TABLE_ID)
        catalog_table = catalog.load_table(self.CATALOG_TABLE_ID)
        return data_table.scan().to_pandas(), catalog_table.scan().to_pandas()

    def write(self, path: str, data_df: pd.DataFrame, catalog_df: pd.DataFrame):
        """Writes a DataFrame to an Iceberg table."""
        base_path = Path(path)

        if base_path.is_file():
            raise ValueError("Cannot write Iceberg format to a file.")
        base_path.mkdir(parents=True, exist_ok=True)

        catalog = load_catalog(
            self.DEFAULT_NAMESPACE,
            **{
                "type": "sql",
                "uri": f"sqlite:///{base_path / self.SQLITE_CATALOG_FILE_NAME}",
                "warehouse": f"file://{base_path}",
            },
        )
        catalog.create_namespace(self.DEFAULT_NAMESPACE)

        # Writing out
        if "timestamp" in data_df.columns:
            data_df["timestamp"] = data_df["timestamp"].astype("datetime64[us]")

        data_arrow_table = pa.Table.from_pandas(data_df)
        data_table = catalog.create_table(
            self.DATA_TABLE_ID, schema=data_arrow_table.schema
        )
        data_table.append(data_arrow_table)

        catalog_arrow_table = pa.Table.from_pandas(catalog_df)
        catalog_table = catalog.create_table(
            self.CATALOG_TABLE_ID, schema=catalog_arrow_table.schema
        )
        catalog_table.append(catalog_arrow_table)
