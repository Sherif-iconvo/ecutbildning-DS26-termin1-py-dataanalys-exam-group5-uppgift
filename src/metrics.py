import pandas as pd


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


if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    print("Rows before cleaning:", len(df))

    df = clean_data(df)

    print("Rows after cleaning:", len(df))