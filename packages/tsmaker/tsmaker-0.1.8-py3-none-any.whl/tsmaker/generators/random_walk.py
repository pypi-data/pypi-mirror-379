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
from typing import Tuple, Dict

import numpy as np
import pandas as pd
from pandas import DataFrame

from tsmaker import utils

from dataclasses import dataclass

from tsmaker.distribution import Distribution
from tsmaker.maker_settings import MakerSettings


@dataclass
class RandomWalkModel:
    distribution: Distribution
    mean: float
    stdev: float
    laplace_b: float


def generate_random_walk(
    settings: MakerSettings,
    model: RandomWalkModel,
) -> Tuple[DataFrame, DataFrame, Dict]:
    """
    Generate a random walk for a given time period with a specified time stamp and jitter

    :param settings: General settings for generating a time series
    :param model: Random Walk specific parameters.
    """
    timestamps = utils.generate_timestamps_vectorized(settings)
    n_samples = len(timestamps)

    if model.distribution == Distribution.laplace:
        values = np.random.laplace(
            loc=model.mean, scale=model.laplace_b, size=n_samples
        )
    else:
        values = np.random.normal(loc=model.mean, scale=model.stdev, size=n_samples)
    values = np.cumsum(values)

    df = DataFrame(
        {
            "metric_id": np.repeat(1002, n_samples),
            "timestamp": timestamps,
            "value": values,
        }
    )

    return (
        df,
        pd.DataFrame(
            {
                "metric_id": 1002,
                "name": "random walk",
                "tags": {"generator": "random_walk"},
            }
        ),
        {},
    )
