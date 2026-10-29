"""
src/metrics.py

Tillhandahåller analytiska funktioner för bearbetning av e-handelstransaktionsdata.
(Förutsatt att indata-DataFrame redan har rengjorts av io_utils.py).

- date_range(): Returnerar det tidigaste och senaste beställningsdatumet i datamängden.
- orders_per_month(): Beräknar det totala antalet beställningar grupperat per kalendermånad.
- order_per_week(): Beräknar det totala antalet beställningar per veckodag, sorterat mondag -> Sundag.
- monthly_revenue_summary(): Beräkna månatlig intäktsöversiktsstatistik: summa, medelvärde och orderantal.
- category_performance(): Intäkt, enheter och antal ordrar per kategori. by_month=True grupperar per månad och kategori.
- city_performance(): Intäkt, enheter och AOV per stad. by_month=True grupperar per månad och stad.

"""


import pandas as pd

def date_range(df: pd.DataFrame) -> tuple[pd.Timestamp, pd.Timestamp]:           # period covered
    return df["date"].min(), df["date"].max()            

def orders_per_month(df: pd.DataFrame) -> pd.Series:
    df_temp = df.copy()
    df_temp["period"] = df_temp["date"].dt.to_period("M")
    monthly_orders = df_temp["period"].value_counts().sort_index()               # orders per month
    monthly_orders.name = "month_orders"
    return monthly_orders

def order_per_week(df: pd.DataFrame) -> pd.Series:
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]
    weekday_orders = df["date"].dt.day_name().value_counts().reindex(weekdays)   # orders per weekday
    weekday_orders.name = "Weekday_orders"
    return weekday_orders

def monthly_revenue_summary(df: pd.DataFrame) -> pd.DataFrame:                   # sum: total revenue per month/ mean: average order value (AOV) per month / count: orders per month
    df_temp = df.copy()
    df_temp["period"] = df_temp["date"].dt.to_period("M")
    monthly = df_temp.groupby(df_temp["period"])["revenue"].agg(["sum", "mean", "count"]) 
    return monthly

def category_performance(df: pd.DataFrame, by_month: bool = False) -> pd.DataFrame:
    df_temp = df.copy()
    if by_month:                                                                  # total revenue, units sold, and order count per product category per month
        df_temp["period"] = df_temp["date"].dt.to_period("M")
        group_cols = ["period", "category"]
        sort_values_by = ["period", "total_revenue"]
        ascending_arr = [True, False]
    else:                                                                         # total revenue, units sold, and order count per product category
        group_cols = ["category"]
        sort_values_by = ["total_revenue"]
        ascending_arr = [False]

    result = (df_temp.groupby(group_cols)                    
                       .agg
                       (
                           total_revenue = ("revenue", "sum"), 
                           units_sold = ("units", "sum"), 
                           order_count = ("order_id", "count"),
                           )
                           .sort_values(by=sort_values_by, ascending=ascending_arr)
                    )
    
    return result


def city_performance(df: pd.DataFrame, by_month: bool = False) -> pd.DataFrame:
    df_temp = df.copy()
    if by_month:                                                                    # total revenue, units sold, and average order value per product city per month
        df_temp["period"] = df_temp["date"].dt.to_period("M")
        group_cols = ["period", "city"]
        sort_values_by = ["period", "total_revenue"]
        ascending_arr = [True, False]
    else:                                                                           # total revenue, units sold, and average order value per product city
        group_cols = ["city"]
        sort_values_by = ["total_revenue"]
        ascending_arr = [False]

    result = (df_temp.groupby(group_cols)                    
                       .agg
                       (
                           total_revenue = ("revenue", "sum"), 
                           units_sold = ("units", "sum"), 
                           aov = ("revenue", "mean"),
                           )
                           .sort_values(by=sort_values_by, ascending=ascending_arr)
                    )
    
    return result