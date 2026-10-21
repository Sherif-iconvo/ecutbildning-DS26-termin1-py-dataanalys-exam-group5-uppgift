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
    
    df.columns = (df.columns
                  .str.strip()
                  .str.replace(" ", "_")
                  .str.lower())

    #Types
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["order_id"] = pd.to_numeric(df["order_id"], errors="coerce").astype("Int64")
    df["price"] = pd.to_numeric(df["price"], errors="coerce").astype("float64")
    df["units"] = pd.to_numeric(df["units"], errors="coerce").astype("Int64")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").astype("float64")

    # String Normalization
    df["city"] = df["city"].str.strip().str.title()
    df["category"] = df["category"].str.strip().str.title()
    
    # Quality Checks & Filtering
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    df = df[(df["price"] > 0) & (df["units"] > 0)]
    
    expected_revenue = df["price"] * df["units"]
    df = df[np.isclose(df["revenue"], expected_revenue, atol=0.01)]
    # a NumPy function that checks whether two numbers (or two columns of numbers) are equal to each other within a small tolerance (np.isclose(a, b, atol=tolerance).
    
    df = df.dropna(subset=["date", "order_id"])
    
    return df

# 3. CONVENIENCE WRAPPER (Combines both for quick usage)
def load_and_clean_transactions(filepath: str | Path | None = None) -> pd.DataFrame:
    raw_df = load_raw_transactions(filepath)
    return clean_transactions(raw_df)