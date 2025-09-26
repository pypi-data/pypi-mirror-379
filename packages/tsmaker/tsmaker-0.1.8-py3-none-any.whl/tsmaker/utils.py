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
import numpy as np

from tsmaker.maker_settings import MakerSettings


def generate_timestamps(settings: MakerSettings):
    """
    Generates a list of timestamps between a start and end date.

    Args:
        :param settings: General settings for generating timestamps (start, end, step jitter).

    Returns:
        list: A list of datetime objects.
    """
    timestamps = []
    current_time = settings.start_date
    while current_time <= settings.end_date:
        timestamps.append(current_time)
        # Add jitter to the time step
        step = settings.time_step + np.random.randint(
            -settings.jitter, settings.jitter + 1
        )
        current_time += pd.to_timedelta(step, unit="s")
    return timestamps


def generate_timestamps_vectorized(settings: MakerSettings):
    """
    Generates a list of timestamps between a start and end date.

    This function uses vectorized functions from NumPy to speed up the generation process.

    Args:
        :param settings: General settings for generating timestamps (start, end, step jitter).

    Returns:
        list: A list of datetime objects.
    """
    # Calculate the number of steps
    total_seconds = (settings.end_date - settings.start_date).total_seconds()
    num_steps = int(total_seconds // settings.time_step) + 1

    # Generate steps with jitter
    steps = np.arange(num_steps) * settings.time_step
    jitter_values = np.random.randint(
        -settings.jitter, settings.jitter + 1, size=num_steps
    )
    steps_with_jitter = steps + jitter_values

    # Convert to timestamps
    timestamps = pd.to_datetime(steps_with_jitter, unit="s", origin=settings.start_date)

    # Filter timestamps that exceed end_date
    timestamps = timestamps[timestamps <= settings.end_date]

    return timestamps.tolist()


if __name__ == "__main__":

    def main():
        import timeit
        from datetime import datetime

        # Define parameters
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 2, 1)
        time_step = 60  # 1 minute
        jitter = 5  # 5 seconds

        # Time the function
        time_taken = timeit.timeit(
            lambda: generate_timestamps(
                MakerSettings(start_date, end_date, time_step, jitter)
            ),
            number=200,
        )
        print(f"Time taken: {time_taken:.4f} seconds")

        # Time the vectorized function
        time_taken_vectorized = timeit.timeit(
            lambda: generate_timestamps_vectorized(
                MakerSettings(start_date, end_date, time_step, jitter)
            ),
            number=200,
        )
        print(f"Time taken (vectorized): {time_taken_vectorized:.4f} seconds")

    main()
