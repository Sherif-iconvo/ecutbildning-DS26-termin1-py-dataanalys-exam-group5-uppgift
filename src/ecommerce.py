import pandas as pd


class EcommerceAnalyzer:
    """
    Klass för analys av e-handelsdata.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_total_revenue(self) -> float:
        """
        Calculate and return the total revenue.
        """
        return self.df["revenue"].sum()


if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    analyzer = EcommerceAnalyzer(df)

    print("Total revenue:")
    print(analyzer.get_total_revenue())
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
import matplotlib.pyplot as plt
import pandas as pd
import src.metrics as metrics       # or from src import metrics
import src.viz as viz
from src.io_utils import load_and_clean_transactions    # Import the wrapper function from io_utils

class EcommerceAnalyzer:
    # --- io_utils Delegation ---
    def __init__(self, filepath: str | Path | None = None) -> None:
        self.df: pd.DataFrame = load_and_clean_transactions(filepath)   # the cleaned DataFrame is assigned to self.df. This makes the cleaned dataset persist in memory for as long as your object exists.

    # --- Metrics Delegation-metoder---
    # --- Edvins fråga (1): Vad säljer? ---
    def revenue_by_category(self):
        return metrics.revenue_by_category(self.df)
    
    # --- Sherifs fråga (3): När säljer vi? ---
    def date_range(self) -> tuple[pd.Timestamp, pd.Timestamp]: 
        return metrics.date_range(self.df)

    def orders_per_weekday(self) -> pd.Series:
        return metrics.orders_per_weekday(self.df)

    def orders_per_month(self) -> pd.Series:
        return metrics.orders_per_month(self.df)

    def weekly_revenue_summary(self) -> pd.Series:
        return metrics.weekly_revenue_summary(self.df)
    
    def weekday_revenue_summary(self) -> pd.DataFrame:
        return metrics.weekday_revenue_summary(self.df)

    def monthly_revenue_summary(self) -> pd.DataFrame:
        return metrics.monthly_revenue_summary(self.df)

    def monthly_revenue_change(self) -> pd.DataFrame:
        return metrics.monthly_revenue_change(self.df)


    # --- Sherifs fråga (1-2 + tid/månad): Vad säljer vi? / Var säljer vi? ---
    def category_performance(self, by_month: bool = False) -> pd.DataFrame:
        return metrics.category_performance(self.df, by_month)

    def city_performance(self, by_month: bool = False) -> pd.DataFrame:
        return  metrics.city_performance(self.df, by_month)
    

    # --- Visualization Delegation ---

    # --- Visualization Delegation-metoder ---
    def plot_weekday_overview(self) -> plt.figure:
        return viz.plot_weekday_overview(self.weekday_revenue_summary())

    def plot_weekly_revenue(self) -> plt.figure:
        return viz.plot_weekly_rev(self.weekly_revenue_summary())

    def plot_monthly_overview(self) -> plt.figure:
        return viz.plot_monthly_overview(self.monthly_revenue_change())

    def plot_category_trends(self) -> plt.figure:
        return viz.plot_category_trends(self.category_performance(by_month=True))

    def plot_city_trends(self) -> plt.figure:
        return viz.plot_city_trends(self.city_performance(by_month=True))
    
    # --- Mahmouds fråga (6): Eventuella avvikelser

    def identify_outliers(self, column: str) -> tuple[pd.DataFrame, float, float]:
            return metrics.identify_outliers(self.df, column)
    
    def plot_outliers_boxplot(self, column):
            return viz.plot_outliers_boxplot(self.df, column)

    def plot_outliers_by_group(self, column, group_column):
            outliers, _,_ = self.identify_outliers(column)

            return viz.plot_outliers_by_group(
             self.df, outliers, group_column
    )

# --- Ona fråga 2 ---
        
    def plot_city_revenue_bar(self) -> plt.figure:
        return viz.plot_city_revenue_bar(self.city_performance())
