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
import argparse
from datetime import datetime

from tsmaker.persistence import persistence


def parse_arguments():
    # Building parser
    parser = argparse.ArgumentParser(
        description="Generate time series data.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    _build_time_arguments(parser)
    _build_generator_arguments(parser)
    _add_random_walk_arguments(parser)
    _add_fourier_arguments(parser)
    _add_stock_market_arguments(parser)
    _add_grocery_store_arguments(parser)
    _add_output_arguments(parser)

    return parser.parse_args()


def _add_output_arguments(parser):
    out_group = parser.add_argument_group("Output")
    out_group.add_argument(
        "--output-format", choices=persistence.FILE_FORMAT_MAP.keys(), default="csv"
    )
    out_group.add_argument("--output-path", type=str, default="output")
    out_group.add_argument(
        "--visualize",
        action="store_true",
        help="Display a plot of the data instead of saving to a file.",
    )


def _add_grocery_store_arguments(parser):
    grocery_group = parser.add_argument_group("Grocery Sales Options")
    grocery_group.add_argument("--num-stores", type=int, default=3, help="Default = 3")
    grocery_group.add_argument(
        "--num-customers", type=int, default=100, help="Default = 100"
    )
    grocery_group.add_argument(
        "--avg-trips-per-day", type=int, default=50, help="Default = 50"
    )


def _add_stock_market_arguments(parser):
    stock_group = parser.add_argument_group("Stock Market Options")
    stock_group.add_argument("--num-series", type=int, default=10)
    stock_group.add_argument(
        "--independent-fraction", type=float, default=0.8, help="Default = 0.8"
    )
    stock_group.add_argument("--var-lags", type=int, default=5)


def _add_fourier_arguments(parser):
    fourier_group = parser.add_argument_group("Fourier Options")
    fourier_group.add_argument("--fourier-coeffs", type=int, default=10)
    fourier_group.add_argument("--fourier-min-period", type=str, default="60s")
    fourier_group.add_argument("--fourier-max-period", type=str, default="1d")
    fourier_group.add_argument(
        "--fourier-period-spacing",
        choices=["linear", "exponential"],
        default="linear",
    )


def _add_random_walk_arguments(parser):
    random_walk_group = parser.add_argument_group("Random Walk Options")
    random_walk_group.add_argument("--walk-mean", type=float, default=0.0)
    random_walk_group.add_argument("--walk-std", type=float, default=1.0)
    random_walk_group.add_argument("--walk-laplace-b", type=float, default=1.0)
    random_walk_group.add_argument(
        "--walk-distribution",
        choices=["gaussian", "laplace"],
        default="gaussian",
    )


def _build_generator_arguments(parser):
    gen_group = parser.add_mutually_exclusive_group(required=True)
    gen_group.add_argument("--random", choices=["gaussian", "uniform", "exponential"])
    gen_group.add_argument("--random-walk", action="store_true")
    gen_group.add_argument("--arima", type=str)
    gen_group.add_argument("--fourier", action="store_true")
    gen_group.add_argument("--apartment", action="store_true")
    gen_group.add_argument("--stock-market", action="store_true")
    gen_group.add_argument("--grocery-sales", action="store_true")


def _build_time_arguments(parser):
    time_group = parser.add_argument_group("Time Generation")
    time_group.add_argument(
        "--start-date",
        type=lambda s: datetime.strptime(s, "%Y-%m-%d"),
        required=True,
    )
    time_group.add_argument(
        "--end-date",
        type=lambda s: datetime.strptime(s, "%Y-%m-%d"),
        required=True,
    )
    time_group.add_argument(
        "--time-step", type=int, default=600, help="Default = 600 seconds"
    )
    time_group.add_argument("--jitter", type=int, default=0, help="Default = 0")
