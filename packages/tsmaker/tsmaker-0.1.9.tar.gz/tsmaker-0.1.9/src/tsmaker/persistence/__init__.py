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
import json
from abc import ABC, abstractmethod
from typing import Tuple, Any, Dict

import pandas as pd


class Persistence(ABC):
    @abstractmethod
    def read(self, path) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Reads the data and catalog dataframes from the given location.

        :param path: The location where the data should be stored, typically a directory.
        :return: Data and Catalog Dataframes
        """
        pass

    @abstractmethod
    def write(self, path, data_df, catalog_df):
        """
        Writes out the data and catalog dataframes to the requested location.

        :param path: Where to store, typically a directory
        :param data_df: Time Series Data Dataframe
        :param catalog_df: Catalog Dataframe
        """
        pass

    def write_metadata(self, path: str, metadata: Dict[str, Any]):
        """
        Writes a metadata dictionary to a JSON file.
        """
        with open(path, "w") as f:
            json.dump(metadata, f, indent=2)

    def read_metadata(self, path: str) -> Dict[str, Any]:
        """
        Reads metadata dictionary from a JSON file.
        """
        with open(path, "r") as f:
            return json.loads("\n".join(f.readlines()))
