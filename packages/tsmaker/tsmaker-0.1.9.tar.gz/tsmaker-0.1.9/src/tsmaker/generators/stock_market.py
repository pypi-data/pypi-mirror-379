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

import itertools
import random
import string
from dataclasses import dataclass

import numpy as np
import pandas as pd

from tsmaker.generators import random_walk
from tsmaker.generators.random_walk import RandomWalkModel
from tsmaker import utils
from tsmaker.distribution import Distribution
from tsmaker.maker_settings import MakerSettings


@dataclass
class StockMarketModel:
    num_series: int
    independent_fraction: float
    var_lags: int


def _generate_ticker_symbols(n):
    """Generates n unique, 4-letter stock ticker symbols."""
    tickers = set()
    while len(tickers) < n:
        tickers.add("".join(random.choices(string.ascii_uppercase, k=4)))
    return list(tickers)


def generate_stock_market(settings: MakerSettings, model: StockMarketModel):
    """Generates stock market data with a catalog."""
    num_independent = max(1, int(model.num_series * model.independent_fraction))

    tickers = _generate_ticker_symbols(model.num_series)
    independent_tickers = tickers[:num_independent]
    dependent_tickers = tickers[num_independent:]

    timestamps = utils.generate_timestamps_vectorized(settings)
    n_samples = len(timestamps)

    # 1. Build Catalog and Metadata
    catalog_df, metadata, ticker_to_id = _generate_catalog_and_meta_data(
        dependent_tickers,
        independent_tickers,
        num_independent,
        model.var_lags,
    )

    # 2. Generate Series
    # Use a temporary wide DataFrame for easier calculation
    temp_df = pd.DataFrame(index=range(n_samples), columns=tickers)
    initial_prices = np.random.uniform(50, 200, size=model.num_series)

    # Generating random walks for the independent series
    for i, independent_ticker in enumerate(independent_tickers):
        stock_random_walk_model = RandomWalkModel(Distribution.laplace, 0.001, 0.5, 0.5)

        model_data_df = random_walk.generate_random_walk(
            settings, stock_random_walk_model
        )[0]
        temp_df[independent_ticker] = model_data_df["value"] + initial_prices[i]

    for t in range(1, n_samples):
        for ticker in dependent_tickers:
            if t < model.var_lags:
                # No value available yet
                continue

            coefficients = metadata["coefficients"][ticker]

            var_value = 0
            coefficient_index = 0
            for independent_ticker in independent_tickers:
                for lag in range(1, model.var_lags + 1):
                    var_value += (
                        coefficients[coefficient_index]
                        * temp_df.loc[t - lag, independent_ticker]
                    )
                    coefficient_index += 1

            temp_df.loc[t, ticker] = var_value + np.random.normal(0, 0.5)

    temp_df = temp_df.clip(lower=0.01)

    # 3. Convert to Long Format
    data_df = temp_df.melt(id_vars=None, var_name="name", value_name="value")
    data_df["metric_id"] = data_df["name"].map(ticker_to_id)
    data_df["timestamp"] = np.tile(timestamps, model.num_series)

    return data_df[["metric_id", "timestamp", "value"]], catalog_df, metadata


def _generate_catalog_and_meta_data(
    dependent_tickers, independent_tickers, num_independent, var_lags
):
    catalog_records = []
    metadata = {
        "var_formulas": {},
        "coefficients": {},
        "independent_series": independent_tickers,
    }
    metric_id_counter = itertools.count(5001)
    ticker_to_id = {}

    for ticker in independent_tickers:
        metric_id = next(metric_id_counter)
        ticker_to_id[ticker] = metric_id
        catalog_records.append(
            {
                "metric_id": metric_id,
                "name": ticker,
                "tags": {"type": "independent", "generator": "random_walk"},
            }
        )

    for ticker in dependent_tickers:
        metric_id = next(metric_id_counter)
        ticker_to_id[ticker] = metric_id
        coefficients = np.random.normal(loc=1, scale=5, size=num_independent * var_lags)
        coefficients = (
            2 * coefficients / np.size(coefficients)
        )  # Custom normalization to get a good effect
        formula = " + ".join(
            [
                f"{coefficient:.4f}*{independent_ticker}(t-{lag_index + 1})"
                for ticker_index, independent_ticker in enumerate(independent_tickers)
                for lag_index, coefficient in enumerate(
                    coefficients[
                        ticker_index * var_lags : (ticker_index + 1) * var_lags
                    ]
                )
            ]
        )
        metadata["var_formulas"][ticker] = formula
        metadata["coefficients"][ticker] = coefficients.tolist()
        catalog_records.append(
            {
                "metric_id": metric_id,
                "name": ticker,
                "tags": {"type": "dependent", "generator": "var", "formula": formula},
            }
        )

    catalog_df = pd.DataFrame(catalog_records)
    return catalog_df, metadata, ticker_to_id
