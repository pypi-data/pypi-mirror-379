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
from typing import Tuple

import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import ArmaProcess

from .. import utils
from ..maker_settings import MakerSettings


def generate_arima(settings: MakerSettings, order: Tuple[int, int, int]):
    """Generates an ARIMA series with a catalog."""
    p, d, q = order

    timestamps = utils.generate_timestamps(settings)
    values = _generate_random_walk(p, d, q, len(timestamps))

    metric_id = 1001

    data_df = pd.DataFrame(
        {"metric_id": metric_id, "timestamp": timestamps, "value": values}
    )

    catalog_df = pd.DataFrame(
        [
            {
                "metric_id": metric_id,
                "name": f"arima_{p}_{d}_{q}",
                "tags": {"generator": "arima", "order": f"({p},{d},{q})"},
            }
        ]
    )

    return data_df, catalog_df, {}


def _generate_random_walk(p: int, d: int, q: int, n_samples: int):
    ar_params = np.array([1] + [-0.5 / p] * p) if p > 0 else np.array([1])
    ma_params = np.array([1] + [0.5 / q] * q) if q > 0 else np.array([1])
    arma_process = ArmaProcess(ar_params, ma_params)
    values = arma_process.generate_sample(nsample=n_samples)
    for _ in range(d):
        values = np.cumsum(values)
    return values
