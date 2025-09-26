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
import pyarrow.parquet
import pyarrow as pa
from tsmaker.persistence.file_persistence import FilePersistence


class ParquetPersistence(FilePersistence):
    def __init__(self):
        super().__init__(
            lambda path, df: pyarrow.parquet.write_table(
                pa.Table.from_pandas(df), path
            ),
            lambda path: pyarrow.parquet.read_table(path).to_pandas(),
            "parquet",
        )
