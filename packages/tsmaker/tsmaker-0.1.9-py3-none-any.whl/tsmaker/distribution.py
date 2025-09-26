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
from enum import Enum


class Distribution(Enum):
    """Listing different probability distributions."""

    gaussian = 1
    laplace = 2
    poisson = 3
    exponential = 4
    uniform = 5

    @staticmethod
    def from_string(distribution_str: str) -> "Distribution":
        """Create a Distributions enum from a string.

        Args:
            distribution_str (str): The string representation of the distribution.

        Returns:
            Distribution: The corresponding Distributions enum value.

        Raises:
            ValueError: If the string does not match any known distribution.
        """
        try:
            return Distribution[distribution_str.lower()]
        except KeyError:
            raise ValueError(f"Unknown distribution: {distribution_str}")
