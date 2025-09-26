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

import sys

from tsmaker.persistence import persistence
from tsmaker.argument_parsing import parse_arguments
from tsmaker.distribution import Distribution
from tsmaker.generators import apartment as apartment_gen, random_walk
from tsmaker.generators import arima as arima_gen
from tsmaker.generators import fourier as fourier_gen
from tsmaker.generators import grocery_sales as grocery_sales_gen
from tsmaker.generators import random as random_gen
from tsmaker.generators import stock_market as stock_market_gen
from tsmaker.generators.fourier import FourierModel
from tsmaker.generators.grocery_sales import GroceryModel
from tsmaker.generators.random_walk import RandomWalkModel
from tsmaker.generators.stock_market import StockMarketModel
from tsmaker.maker_settings import MakerSettings
from tsmaker.plotting import visualize_data


def main():
    """
    Entry point of the Command Line Interface (CLI) of `tsmaker`.

    Sets up the parser, parses the arguments and calls the appropriate generator.
    """
    args = parse_arguments()

    settings = MakerSettings(
        args.start_date, args.end_date, args.time_step, args.jitter
    )

    data_df, catalog_df, metadata = None, None, None
    generator_name = ""

    # --- Call the appropriate generator ---
    if args.random:
        generator_name = f"random_{args.random}"
        generator_func = getattr(random_gen, f"generate_{args.random}")

        data_df, catalog_df, metadata = generator_func(settings)
    elif args.random_walk:
        generator_name = "random_walk"
        data_df, catalog_df, metadata = random_walk.generate_random_walk(
            settings,
            RandomWalkModel(
                Distribution.from_string(args.walk_distribution),
                args.walk_mean,
                args.walk_std,
                args.walk_laplace_b,
            ),
        )
    elif args.arima:
        try:
            order = tuple(map(int, args.arima.split(",")))
            if len(order) != 3:
                raise ValueError
        except ValueError:
            print(f"Error: Invalid ARIMA order format '{args.arima}'.", file=sys.stderr)
            sys.exit(1)

        generator_name = f"arima_{'_'.join(map(str, order))}"
        data_df, catalog_df, metadata = arima_gen.generate_arima(settings, order)
    elif args.fourier:
        generator_name = "fourier"
        fourier_model = FourierModel(
            args.fourier_coeffs,
            args.fourier_min_period,
            args.fourier_max_period,
            args.fourier_period_spacing,
        )
        data_df, catalog_df, metadata = fourier_gen.generate_fourier(
            settings, fourier_model
        )
    elif args.apartment:
        generator_name = "apartment"
        data_df, catalog_df, metadata = apartment_gen.generate_apartment_sensors(
            settings
        )
    elif args.stock_market:
        generator_name = "stock_market"
        data_df, catalog_df, metadata = stock_market_gen.generate_stock_market(
            settings,
            StockMarketModel(args.num_series, args.independent_fraction, args.var_lags),
        )
    elif args.grocery_sales:
        generator_name = "grocery_sales"
        data_df, catalog_df, metadata = grocery_sales_gen.generate_grocery_sales(
            settings,
            GroceryModel(args.num_stores, args.num_customers, args.avg_trips_per_day),
        )

    # --- Handle the output ---
    if data_df is None:
        print("Error: Could not generate data.", file=sys.stderr)
        sys.exit(1)

    if args.visualize:
        visualize_data(data_df, catalog_df, generator_name)
    else:
        persistence.save_time_series(
            data_df,
            catalog_df,
            metadata=metadata,
            base_path=args.output_path,
            file_format=args.output_format,
        )


if __name__ == "__main__":
    main()
