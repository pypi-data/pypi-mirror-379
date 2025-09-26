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

import datetime
from dataclasses import dataclass
from typing import Any, Dict, Tuple

import pandas as pd
import numpy as np
import random
import itertools

from tsmaker.maker_settings import MakerSettings

# --- Master Data & Configuration ---
# In a real application, this would be loaded from external files (e.g., JSON, YAML).

PRODUCTS = {
    "Apple": {"dept": "Fruit", "price": 0.50},
    "Banana": {"dept": "Fruit", "price": 0.30},
    "Milk": {"dept": "Dairy", "price": 1.20},
    "Cheese": {"dept": "Dairy", "price": 4.50},
    "Bread": {"dept": "Bakery", "price": 2.10},
    "Chicken Breast": {"dept": "Meat", "price": 8.00},
    "Salmon Fillet": {"dept": "Meat", "price": 12.50},
    "Tomatoes": {"dept": "Vegetables", "price": 3.00},
    "Onions": {"dept": "Vegetables", "price": 1.50},
    "Cereal": {"dept": "Pantry", "price": 3.80},
    "Pasta": {"dept": "Pantry", "price": 1.80},
    "Soda": {"dept": "Drinks", "price": 1.50},
    "Beer": {"dept": "Drinks", "price": 5.50},
}

LOCATIONS = {
    "Store A": {"city": "Hasselt", "region": "Flanders", "country": "Belgium"},
    "Store B": {"city": "Genk", "region": "Flanders", "country": "Belgium"},
    "Store C": {"city": "Antwerp", "region": "Flanders", "country": "Belgium"},
}

# --- Entity Classes ---


class Store:
    """Represents a single grocery store with its own location and inventory."""

    def __init__(self, name, location_info):
        self.name = name
        self.location = location_info
        # Each store has 80% of the master product list
        self.inventory = random.sample(list(PRODUCTS.keys()), int(len(PRODUCTS) * 0.8))


class Customer:
    """Represents a customer with a profile and shopping preferences."""

    def __init__(self, customer_id, all_store_names):
        self.id = customer_id
        self.profile = {
            "age_group": random.choice(["18-30", "31-50", "51+"]),
            "sex": random.choice(["M", "F"]),
        }
        self.preferred_store = random.choice(all_store_names)


# --- Simulation Engine ---


class GrocerySimulation:
    """Encapsulates the entire grocery sales simulation."""

    def __init__(self, num_stores, num_customers):
        self._initialize_entities(num_stores, num_customers)
        self._prebuild_catalog()

    def _initialize_entities(self, num_stores, num_customers):
        """Creates the stores and customers for the simulation."""
        store_names = list(LOCATIONS.keys())[:num_stores]
        self.stores = {name: Store(name, LOCATIONS[name]) for name in store_names}
        self.customers = [Customer(i, store_names) for i in range(num_customers)]

    def _prebuild_catalog(self):
        """Creates a master catalog of all possible metric IDs before the simulation."""
        self.catalog_records = []
        self.tag_to_id_map = {}
        metric_id_counter = itertools.count(1000)

        for store in self.stores.values():
            for item_name in store.inventory:
                for customer in self.customers:
                    base_tags = {
                        "store": store.name,
                        "department": PRODUCTS[item_name]["dept"],
                        "item_name": item_name,
                        "city": store.location["city"],
                        "country": store.location["country"],
                        "customer_id": customer.id,
                        "customer_age_group": customer.profile["age_group"],
                    }

                    for metric in ["sales_amount", "sales_price"]:
                        tags = {**base_tags, "metric": metric}
                        tag_key = frozenset(tags.items())

                        metric_id = next(metric_id_counter)
                        self.tag_to_id_map[tag_key] = metric_id
                        self.catalog_records.append(
                            {
                                "metric_id": metric_id,
                                "name": metric,
                                "tags": {
                                    k: v for k, v in tags.items() if k != "metric"
                                },
                            }
                        )
        self.catalog_df = pd.DataFrame(self.catalog_records)

    def _simulate_shopping_trip(self, timestamp):
        """Simulates a single customer's shopping trip and yields sales events."""
        customer = random.choice(self.customers)
        store_name = (
            customer.preferred_store
            if random.random() < 0.8
            else random.choice(list(self.stores.keys()))
        )
        store = self.stores[store_name]

        cart_size = random.randint(1, 10)
        for _ in range(cart_size):
            item_name = random.choice(store.inventory)
            item_info = PRODUCTS[item_name]
            amount = (
                random.randint(1, 3) if item_info["dept"] in ["Fruit", "Drinks"] else 1
            )

            base_tags = {
                "store": store.name,
                "department": item_info["dept"],
                "item_name": item_name,
                "city": store.location["city"],
                "country": store.location["country"],
                "customer_id": customer.id,
                "customer_age_group": customer.profile["age_group"],
            }

            # Yield amount event
            amount_tags_key = frozenset({**base_tags, "metric": "sales_amount"}.items())
            yield {
                "metric_id": self.tag_to_id_map[amount_tags_key],
                "timestamp": timestamp,
                "value": amount,
            }

            # Yield price event
            price_tags_key = frozenset({**base_tags, "metric": "sales_price"}.items())
            yield {
                "metric_id": self.tag_to_id_map[price_tags_key],
                "timestamp": timestamp,
                "value": item_info["price"] * amount,
            }

    def run(self, start_date, end_date, avg_trips_per_day):
        """Runs the full simulation and returns the sales and catalog DataFrames."""
        sales_records = []
        total_days = (end_date - start_date).days + 1

        for day_num in range(total_days):
            current_date = start_date.date() + datetime.timedelta(days=day_num)
            num_trips = np.random.poisson(avg_trips_per_day)

            for _ in range(num_trips):
                random_second = random.randint(8 * 3600, 20 * 3600)
                timestamp = datetime.datetime.combine(
                    current_date, datetime.time()
                ) + datetime.timedelta(seconds=random_second)
                if timestamp > end_date:
                    continue
                sales_records.extend(self._simulate_shopping_trip(timestamp))

        sales_df = pd.DataFrame(sales_records)
        return sales_df, self.catalog_df


# --- Main Generator Function ---


@dataclass
class GroceryModel:
    num_stores: int
    num_customers: int
    avg_trips_per_day: int


def generate_grocery_sales(
    settings: MakerSettings, model: GroceryModel
) -> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, Any]]:
    """
    Generates a sparse, high-cardinality grocery sales dataset.

    Returns:
        tuple: (sales_df, catalog_df)
    """
    if model.num_stores > len(LOCATIONS):
        raise ValueError(
            f"num_stores cannot exceed the number of available locations ({len(LOCATIONS)})."
        )

    simulation = GrocerySimulation(model.num_stores, model.num_customers)
    sales_df, catalog_df = simulation.run(
        settings.start_date,
        settings.end_date,
        model.avg_trips_per_day,
    )

    metadata = {
        "num_stores": model.num_stores,
        "num_customers": model.num_customers,
        "avg_trips_per_day": model.avg_trips_per_day,
    }

    if sales_df.empty:
        return (
            pd.DataFrame(columns=["metric_id", "timestamp", "value"]),
            catalog_df,
            metadata,
        )
    return sales_df, catalog_df, metadata
