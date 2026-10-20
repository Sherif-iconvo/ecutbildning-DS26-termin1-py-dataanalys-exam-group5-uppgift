import pandas as pd
import matplotlib.pyplot as plt

def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rensar datasetet från saknade värden och dubletter.
    """

    df = df.drop_duplicates()
    df = df.dropna()

    return df


def check_data_quality(df: pd.DataFrame) -> None:
    """
    Kontrollerar saknade och ovanliga värden.
    """

    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nNegative revenues:")
    print((df["revenue"] < 0).sum())

    print("\nNegative units:")
    print((df["units"] < 0).sum())

def calculate_order_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Beräknar ordervärde per order.
    """

    df["calculated_revenue"] = df["price"] * df["units"]

    return df


def revenue_by_city(df: pd.DataFrame) -> pd.Series:
    """
    Beräknar total intäkt per stad.
    """

    return (
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def revenue_by_month(df: pd.DataFrame) -> pd.Series:
    """
    Beräknar total intäkt per månad.
    """

    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    monthly_revenue = (
        df.groupby(df["date"].dt.month)["revenue"]
        .sum()
    )

    return monthly_revenue

def plot_revenue_by_city(city_revenue: pd.Series) -> None:
    """
    Skapar ett stapeldiagram för försäljning per stad.
    """

    plt.figure(figsize=(8, 5))

    city_revenue.plot(
        kind="bar",
        color="skyblue"
    )

    plt.title("Revenue by City")
    plt.xlabel("City")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.show()

def plot_revenue_by_category(category_revenue: pd.Series) -> None:
    """
    Skapar ett stapeldiagram för försäljning per kategori.
    """

    plt.figure(figsize=(8, 5))

    category_revenue.plot(
        kind="bar",
        color="lightgreen"
    )

    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.show()


def plot_revenue_by_month(monthly_revenue: pd.Series) -> None:
    """
    Visualiserar intäkter över tid.
    """

    plt.figure(figsize=(8, 5))

    monthly_revenue.plot(
        kind="line",
        marker="o",
        color="purple"
    )

    plt.title("Revenue by Month")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    print("Rows before cleaning:", len(df))

    df = clean_data(df)

    print("Rows after cleaning:", len(df))

    check_data_quality(df)

df = calculate_order_value(df)

print(
    df[
        ["order_id", "price", "units", "revenue", "calculated_revenue"]
    ].head()
)

city_revenue = revenue_by_city(df)

print("\nRevenue by city:")

print(city_revenue)

plot_revenue_by_city(city_revenue)

category_revenue = revenue_by_category(df)

print("\nTop categories:")

print(category_revenue)

plot_revenue_by_category(category_revenue)

monthly_revenue = revenue_by_month(df)

print("\nRevenue by month:")

print(monthly_revenue)

plot_revenue_by_month(monthly_revenue)