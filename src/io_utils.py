import pandas as pd


def check_data_quality(table):
    """Funktion som kontrollerar datakvaliteten baserat på testerna i mahmoud-analysis.ipynb.

    Den varnar om det finns fel, men raderar ingenting tyst.
    Parameter:
        table (pd.DataFrame): Tabellen som ska kontrolleras.
    """
    # 1. Kontrollera saknade värden (NaN)
    missing = table.isna().sum().sum()
    if missing > 0:
        print(f"Varning: Det finns {missing} saknade värden i datan!")
    else:
        print("Inga saknade värden hittades.")

    # 2. Kontrollera dubbletter i hela tabellen och i order_id
    duplicates = table.duplicated().sum()
    duplicate_orders = table["order_id"].duplicated().sum()
    if duplicates > 0 or duplicate_orders > 0:
        print(
            f"Varning: Det finns dubbletter! (Hela rader: {duplicates}, order_id: {duplicate_orders})"
        )
    else:
        print("Inga dubbletter hittades i varken rader eller order_id.")

    # 3. Kontrollera att pris och antal är positiva (större än 0)
    bad_price = (table["price"] <= 0).sum()
    bad_units = (table["units"] <= 0).sum()
    if bad_price > 0 or bad_units > 0:
        print(
            f"Varning: Ogiltiga värden hittades! (Pris <= 0: {bad_price}, Antal <= 0: {bad_units})"
        )
    else:
        print("Alla priser och antal (units) är positiva.")

    # 4. Kontrollera att datum kan tolkas korrekt
    invalid_dates = pd.to_datetime(table["date"], errors="coerce").isna().sum()
    if invalid_dates > 0:
        print(f"Varning: Det finns {invalid_dates} felaktiga datum i datan!")
    else:
        print("Alla datum har ett giltigt format.")

    # 5. Kontrollera att revenue stämmer med price * units
    expected_revenue = table["price"] * table["units"]
    revenue_diff = (table["revenue"] - expected_revenue).abs()
    bad_revenue = (revenue_diff > 0.01).sum()
    if bad_revenue > 0:
        print(
            f"Varning: Det finns {bad_revenue} rader där revenue inte stämmer med price * units!"
        )
    else:
        print("Revenue stämmer överens med price * units på alla rader.")

    return table
''' 
This module handles reading the CSV file, parsing datatypes, and applying all
 data quality checks.
 
 1) load_raw_transactions(): I/O Responsibility - Reads raw ecommerce transaction data from CSV without cleaning.
  - we will anchor the path to the module file with pathlib (to dynamically locate files relative to the location of the Python script)
 
 2) clean_transactions(): Data Cleaning Responsibility - Applies datatype casting, text normalization, and quality filters to an existing DataFrame.

 3) load_and_clean_transactions(): Reads CSV file and applies cleaning rules in a single call.

 '''

import pandas as pd
from pathlib import Path
import numpy as np

# 1. READ ONLY (I/O Responsibility)
def load_raw_transactions(filepath: str | Path | None = None) -> pd.DataFrame:
    if filepath is None:
        # 1. Path(__file__) -> /Users/.../project_root/src/io_utils.py
        #   a) __file__ evaluates to a string: "/project/src/io_utils.py"
        #   b) Path("/project/src/io_utils.py") passes that string to the Path class constructor (__init__)
        #   c) The Path class converts the raw string into a Path object, which gives you access to path methods like .parent, .resolve(), and .exists().
        # 2. .resolve()     -> Guarantees an absolute, full path without symlinks
        # 3. .parent.parent moves up two levels to project_root/
        PROJECT_ROOT = Path(__file__).resolve().parent.parent
        filepath = PROJECT_ROOT / "data" / "ecommerce_sales.csv"
    else:
        filepath = Path(filepath)
        # if filepath is already a Path object, this returns a copy of the Path object.

    return pd.read_csv(filepath)


# 2. CLEAN ONLY (Data Cleaning Responsibility)
def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()              # Avoid modifying the original DataFrame in memory

    # (a) Clean the column names (extra spaces, inconsistent capitalization)
    df.columns = (df.columns
                  .str.strip()
                  .str.replace(" ", "_")
                  .str.lower()
                  )
    
    # (b) String Normalization    
    df["city"] = df["city"].str.strip().str.title()
    df["category"] = df["category"].str.strip().str.title()

    # (c) Correct types (safe conversion, bad values become NaN)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["order_id"] = pd.to_numeric(df["order_id"], errors="coerce").astype("Int64")
    df["price"] = pd.to_numeric(df["price"], errors="coerce").astype("float64")
    df["units"] = pd.to_numeric(df["units"], errors="coerce").astype("Int64")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").astype("float64")

    # (d) Quality Checks & Filtering
    # (d-i) Duplicates: order_id should be unique
    df = df.drop_duplicates(subset="order_id")

    # (d-ii) Rows that can't be saved: those with "no order_id" or "no date" (NaN)
    df = df.dropna(subset=["order_id", "date"])

    # (d-iii) Remove zero/negative values (missing values are kept so they can be repaired)
    df = df[
        (df["price"].isna() | (df["price"] > 0)) &
        (df["units"].isna() | (df["units"] > 0)) &
        (df["revenue"].isna() | (df["revenue"] > 0))
        ]
    
    # (d-iv) Repair missing values from revenue = price * units
    df["revenue"] = df["revenue"].fillna(df["price"] * df["units"])
    df["price"]   = df["price"].fillna(df["revenue"] / df["units"])
    df["units"]   = df["units"].fillna((df["revenue"] / df["price"]).round().astype("Int64"))

    # (d-v) Whatever is still missing in price/units/revenue can't be reconstructed, so drop it
    df = df.dropna(subset=["price", "units", "revenue"])

    # (d-vi) Consistency: revenue must equal price * units
    df = df[np.isclose(df["revenue"], df["price"] * df["units"], atol=0.01)]
    
    return df.reset_index(drop=True)

# 3. CONVENIENCE WRAPPER (Combines both for quick usage)
def load_and_clean_transactions(filepath: str | Path | None = None) -> pd.DataFrame:
    raw_df = load_raw_transactions(filepath)
    return clean_transactions(raw_df)
