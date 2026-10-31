from src.ecommerce import EcommerceAnalyzer   # 1. import your class
a = EcommerceAnalyzer()                       # 2. create it → loads + cleans the CSV
print(a.df.shape)                             # 3. print (rows, columns)
print()
print(a.df.info())                            # 4. print each column's type
print()
print("missing values:")
print(a.df.isna().sum())
print()
print("Sample of the cleaned file:")
print(a.df.head())



print()
print("Sanity checks:")
df = a.df
total = df["revenue"].sum()

assert a.orders_per_month().sum() == len(df), "orders_per_month tappar/dubblerar ordrar"
assert a.orders_per_weekday().sum() == len(df), "order_per_weekday tappar/dubblerar ordrar"
assert abs(a.monthly_revenue_summary()["sum"].sum() - total) < 0.01, "monthly_revenue_summary: summan stämmer inte"
assert abs(a.category_performance()["total_revenue"].sum() - total) < 0.01, "category_performance: summan stämmer inte"
assert abs(a.city_performance()["total_revenue"].sum() - total) < 0.01, "city_performance: summan stämmer inte"
assert a.category_performance(by_month=True)["order_count"].sum() == len(df), "category_performance(by_month): fel antal ordrar"
assert abs(a.weekly_revenue_summary().sum() - total) < 0.01, "weekly_revenue_summary: summan stämmer inte"
assert abs(a.weekday_revenue_summary()["sum"].sum() - total) < 0.01, "weekday_revenue_summary: summan stämmer inte"
assert a.weekday_revenue_summary()["count"].sum() == len(df), "weekday_revenue_summary: fel antal ordrar"
assert a.monthly_revenue_change()["count"].sum() == len(df), "monthly_revenue_change: fel antal ordrar"

print("Alla kontroller OK")
