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
import pandas as pd

from tsmaker.persistence.file_persistence import FilePersistence


class TSVPersistence(FilePersistence):
    def __init__(self):
        super().__init__(
            lambda path, df: df.to_csv(path, index=False, sep="\t"),
            lambda path: pd.read_csv(path, sep="\t"),
            "tsv",
        )
