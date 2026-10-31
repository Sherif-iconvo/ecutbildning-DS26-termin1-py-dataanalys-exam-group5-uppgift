''' 
This module handles reading the CSV file, parsing datatypes, and applying all
 data quality checks.
 
 1) load_raw_transactions(): I/O Responsibility - Reads raw ecommerce transaction data from CSV without cleaning.
  - we will anchor the path to the module file with pathlib (to dynamically locate files relative to the location of the Python script)
 
 2) clean_transactions(): Data Cleaning Responsibility - Applies datatype casting, text normalization, and quality filters to an existing DataFrame.

 3) load_and_clean_transactions(): Reads CSV file and applies cleaning rules in a single call.

 '''
import os
import pandas as pd
from pathlib import Path
import numpy as np

def load_data(file_path: str = "data/ecommerce_sales.csv") -> pd.DataFrame:
    """
    Laddar e-handelsdatan från en CSV-fil till en Pandas DataFrame.
    Konverterar 'date' till datetime och säkerställer korrekta datatyper för numeriska fält.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Hittade inte filen på sökvägen: {file_path}")

    df = pd.read_csv(file_path)

    # Issue #9: Tolka 'date' som datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    # Issue #10: Säkerställ korrekta datatyper för price, units och revenue
    numeric_cols = ['price', 'units', 'revenue']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rensar datan: tar bort dubletter och rader med saknade värden
    i kritiska kolumner (date, category, city, revenue).
    Returnerar en rengjord kopia av DataFramen.
    """
    original_len = len(df)

    # Issue #11: Kontroll och rensning av datakvalitet
    df = df.drop_duplicates()

    critical_cols = ['date', 'category', 'city', 'revenue']
    existing_critical = [c for c in critical_cols if c in df.columns]
    df = df.dropna(subset=existing_critical)

    # Se till att revenue och units inte är negativa
    if 'revenue' in df.columns:
        df = df[df['revenue'] >= 0]
    if 'units' in df.columns:
        df = df[df['units'] > 0]

    removed = original_len - len(df)
    if removed > 0:
        print(f"Datarensning: {removed} rader togs bort.")

    return df.reset_index(drop=True)


def load_and_clean_transactions(
    file_path: str = "data/ecommerce_sales.csv"
) -> pd.DataFrame:
    """
    Kombinerad funktion: laddar och rensar datan i ett steg.
    Används av övriga moduler som startpunkt för all analys.
    """
    df = load_data(file_path)
    df = clean_data(df)
    return df


if __name__ == "__main__":
    df = load_and_clean_transactions()
    print("Datat har laddats och rensats framgångsrikt!\n")
    print("Datatyper:")
    print(df.dtypes)
    print(f"\nAntal rader: {len(df)}")
    print("\nFörsta raderna:")
    print(df.head())
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
