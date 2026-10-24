import pandas as pd


def check_data_quality(df: pd.DataFrame) -> None:
    """
    Kontrollerar datakvaliteten.
    """

    print("Missing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nNegative prices:")
    print((df["price"] < 0).sum())

    print("\nNegative units:")
    print((df["units"] < 0).sum())

    print("\nNegative revenue:")
    print((df["revenue"] < 0).sum())

def revenue_by_category(df: pd.DataFrame) -> pd.Series:

    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    check_data_quality(df)
    print("\nRevenue by category:")

    print(revenue_by_category(df))