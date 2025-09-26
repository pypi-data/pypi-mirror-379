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

import numpy as np
import pandas as pd
from .. import utils
from ..maker_settings import MakerSettings


def _generate_random_series(settings: MakerSettings, random_func, name):
    timestamps = utils.generate_timestamps(settings)
    n_samples = len(timestamps)
    values = random_func(size=n_samples)

    metric_id = 1001
    data_df = pd.DataFrame(
        {"metric_id": metric_id, "timestamp": timestamps, "value": values}
    )
    catalog_df = pd.DataFrame(
        [
            {
                "metric_id": metric_id,
                "name": name,
                "tags": {"generator": "random", "distribution": name},
            }
        ]
    )

    return data_df, catalog_df, {"distribution": name}


def generate_gaussian(settings: MakerSettings):
    """Generates a Gaussian random series with a catalog."""
    return _generate_random_series(settings, np.random.normal, "gaussian")


def generate_uniform(settings: MakerSettings):
    """Generates a uniform random series with a catalog."""
    return _generate_random_series(settings, np.random.uniform, "uniform")


def generate_exponential(settings: MakerSettings):
    """Generates an exponential random series with a catalog."""
    return _generate_random_series(settings, np.random.exponential, "exponential")
