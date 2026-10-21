"""
Core class for analyzing e-commerce transaction data.
__init__: Initializes the analyzer by loading and cleaning transaction data. Any other method inside the class can now access this exact same dataset by referencing self.df without having to re-read or re-clean the file from disk

┌─────────────────────────────────────────────────────-----------────────┐
│ 1. User runs: analyzer = EcommerceAnalyzer("data/ecommerce_sales.csv") │
└──────────────────────────────┬────────────────────────-----------──────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────-----───┐
│ 2. __init__() receives filepath = "data/data/ecommerce_sales.csv"│
└──────────────────────────────┬─────────────────────────-----─────┘
                               │
                               ▼
┌────────────────────────────────────────────────────────────------─┐
│ 3. load_and_clean_transactions("data/ecommerce_sales.csv") runs:  │
│    a) load_raw_transactions() reads the raw CSV                   │
│    b) clean_transactions() strips strings, fixes types,           │
│       removes duplicate orders, and drops bad revenue rows        │
└──────────────────────────────┬────────────────────────────------──┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Cleaned DataFrame returned and saved to self.df          │
└─────────────────────────────────────────────────────────────┘

"""


from pathlib import Path
import pandas as pd
from io_utils import load_and_clean_transactions    # Import the wrapper function from io_utils

class EcommerceAnalyzer:
    def __init__(self, filepath: str | Path | None = None) -> None:
        self.df: pd.DataFrame = load_and_clean_transactions(filepath)   # the cleaned DataFrame is assigned to self.df. This makes the cleaned dataset persist in memory for as long as your object exists.



