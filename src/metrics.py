"""
src/metrics.py

Tillhandahåller analytiska funktioner för bearbetning av e-handelstransaktionsdata.
(Förutsatt att indata-DataFrame redan har rengjorts av io_utils.py).

> Sherif fråga (3) nyckeltals-funktioner:
- date_range(): Returnerar det tidigaste och senaste beställningsdatumet i datamängden.
- orders_per_weekday(): Antal ordrar per veckodag, sorterat måndag -> söndag.
- orders_per_month(): Antal ordrar per kalendermånad.
- weekly_revenue_summary(): Total intäkt per vecka.
- weekday_revenue_summary(): Intäkt per veckodag: summa, medelvärde (AOV) och antal ordrar.
- monthly_revenue_summary(): Beräkna månatlig intäktsöversiktsstatistik: summa, medelvärde och orderantal.
- category_performance(): Intäkt, enheter och antal ordrar per kategori. by_month=True grupperar per månad och kategori.
- city_performance(): Intäkt, enheter och AOV per stad. by_month=True grupperar per månad och stad.
- monthly_revenue_change(): Beräkna totala månatliga intäkter och procentuell förändring från månad till månad (MoM %)
> slutet på Sherifs fråga (3) nyckeltals-funktioner.

"""


import pandas as pd

# Sherif fråga (3) nyckeltals-funktioner:
def date_range(df: pd.DataFrame) -> tuple[pd.Timestamp, pd.Timestamp]:           # period covered
    return df["date"].min(), df["date"].max()            

def orders_per_weekday(df: pd.DataFrame) -> pd.Series:
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]
    weekday_orders = df["date"].dt.day_name().value_counts().reindex(weekdays)   # orders per weekday
    weekday_orders.name = "weekday_orders"
    return weekday_orders


def orders_per_month(df: pd.DataFrame) -> pd.Series:                            
    df_temp = df.copy()
    df_temp["period"] = df_temp["date"].dt.to_period("M")
    monthly_orders = df_temp["period"].value_counts().sort_index()               # orders per month
    monthly_orders.name = "month_orders"
    return monthly_orders


def weekly_revenue_summary(df: pd.DataFrame) -> pd.Series:                       # total revenue per week (Mon–Sun)
    return df.set_index("date")["revenue"].resample("W").sum()


def weekday_revenue_summary(df: pd.DataFrame) -> pd.DataFrame:                       # Calculate weekday revenue summary: sum, mean, and order count
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]
    df_temp = df.copy()
    df_temp["weekday"] = df_temp["date"].dt.day_name()
    weekdays_rev_summary = df_temp.groupby("weekday")["revenue"].agg(["sum", "mean", "count"]).reindex(weekdays)
    weekdays_rev_summary["mean"] = weekdays_rev_summary["mean"].round(2)
    return weekdays_rev_summary


def monthly_revenue_summary(df: pd.DataFrame) -> pd.DataFrame:                   # sum: total revenue per month/ mean: average order value (AOV) per month / count: orders per month
    df_temp = df.copy()
    df_temp["period"] = df_temp["date"].dt.to_period("M")
    monthly = df_temp.groupby(df_temp["period"])["revenue"].agg(["sum", "mean", "count"]) 
    monthly["mean"] = monthly["mean"].round(2)
    return monthly


def monthly_revenue_change(df: pd.DataFrame) -> pd.DataFrame:                    # % change from previous month
    monthly = monthly_revenue_summary(df)
    monthly["pct_change"] = (monthly["sum"].pct_change() * 100).round(1)     # % change from previous month
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

# slutet på Sherifs fråga (3) nyckeltals-funktioner.
