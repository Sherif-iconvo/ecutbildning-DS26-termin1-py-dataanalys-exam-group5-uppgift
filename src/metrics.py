import pandas as pd


def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    """
    Beräkna total intäkt per kategori.

    Parameters:
        df (pd.DataFrame): E-handelsdata

    Returns:
        pd.Series: Total intäkt per kategori
    """

    return df.groupby("category")["revenue"].sum()

if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    result = revenue_by_category(df)

    print(result)