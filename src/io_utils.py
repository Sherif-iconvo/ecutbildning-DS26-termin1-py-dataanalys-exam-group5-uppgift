import pandas as pd


REQUIRED = [
    "order_id","date","city","category","price","units","revenue"
]

#Läser CSV filen och gör om datumkolumnen till datetime och kontrollerar så att kolumnerna finns
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Saknade kolumner: {missing}")
    return df


