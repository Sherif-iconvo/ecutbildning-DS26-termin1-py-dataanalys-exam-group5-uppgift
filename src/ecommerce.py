"""
Kärnklass som samordnar inläsning och rensning av data samt analys av ecommerce transaktionsdata, genom att tillhandahålla delegeringsmetoder för mätetal och visualisering.
__init__: Initierar analysatorn genom att läsa in och rensa transaktionsdata. Alla andra metoder i klassen kan nu komma åt exakt samma datamängd genom att referera till `self.df`, utan att behöva läsa in eller rensa filen från disken på nytt.
┌────────────────────────────────────────────┐
│ 1. User runs: analyzer = EcommerceAnalyzer │
└──────────────────────────────┬─────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────----------───┐
│ 2. __init__() receives filepath = None → uses data/ecommerce_sales.csv│
└──────────────────────────────┬─────────────────────────----------─────┘
                               │
                               ▼
┌────────────────────────────────────────────────────────────------─┐
│ 3. load_and_clean_transactions(filepath) runs:  │
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
import src.metrics as metrics       # or from src import metrics
from src.io_utils import load_and_clean_transactions    # Import the wrapper function from io_utils

class EcommerceAnalyzer:
    # --- io_utils Delegation ---
    def __init__(self, filepath: str | Path | None = None) -> None:
        self.df: pd.DataFrame = load_and_clean_transactions(filepath)   # the cleaned DataFrame is assigned to self.df. This makes the cleaned dataset persist in memory for as long as your object exists.

    # --- Metrics Delegation ---

    # --- När säljer vi? ---
    def date_range(self) -> tuple[pd.Timestamp, pd.Timestamp]: 
        return metrics.date_range(self.df)

    def orders_per_month(self) -> pd.Series:
        return metrics.orders_per_month(self.df)

    def order_per_weekday(self) -> pd.Series:
        return metrics.order_per_week(self.df)

    def monthly_revenue_summary(self) -> pd.DataFrame:
        return metrics.monthly_revenue_summary(self.df)


    # --- Vad säljer vi? / Var säljer vi? ---
    def category_performance(self, by_month: bool = False) -> pd.DataFrame:
        return metrics.category_performance(self.df, by_month)

    def city_performance(self, by_month: bool = False) -> pd.DataFrame:
        return  metrics.city_performance(self.df, by_month)

    # --- Visualization Delegation ---