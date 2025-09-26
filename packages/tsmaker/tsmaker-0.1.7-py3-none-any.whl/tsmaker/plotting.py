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

import pandas as pd


def visualize_data(
    data_df: pd.DataFrame, catalog_df: pd.DataFrame, generator_name: str
):
    """
    Displays a plot of the generated time series data.

    :param data_df: Dataframe containing the generated time series data in long-format.
    :param catalog_df: Dataframe containing the catalog of metrics.
    :param generator_name: Name of the generator used to generate the data.
    """

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print(
            "Error: matplotlib is not installed. Please install it to use the --visualize feature (`uv pip install matplotlib`)",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Preparing visualization...")

    if data_df.empty:
        print("Cannot visualize empty dataset.")
        return

    # Merge with catalog to get series names for the legend
    if catalog_df is not None and not catalog_df.empty:
        plot_df = pd.merge(data_df, catalog_df, on="metric_id")
    else:
        plot_df = data_df
        plot_df["name"] = plot_df["metric_id"]

    plt.figure(figsize=(15, 8))

    for name, group in plot_df.groupby("name"):
        # For very sparse data like grocery sales, a scatter plot is better
        if "grocery" in generator_name:
            plt.scatter(group["timestamp"], group["value"], label=name, alpha=0.7)
        else:
            plt.plot(group["timestamp"], group["value"], label=name, alpha=0.8)

    plt.title(f"Generated Time Series: {generator_name.replace('_', ' ').title()}")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout(rect=(0, 0, 0.87, 1))  # Adjust layout to make room for legend
    plt.show()
