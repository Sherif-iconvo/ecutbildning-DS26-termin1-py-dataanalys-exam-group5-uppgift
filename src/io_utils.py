import pandas as pd
import os

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