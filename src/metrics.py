import pandas as pd

def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )