import pandas as pd

#function to get the top 3 catagories and sort them
def top_catagories(df: pd.DataFrame) -> pd.DataFrame:
    return(
        df.groupby("category", dropna=False)["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )