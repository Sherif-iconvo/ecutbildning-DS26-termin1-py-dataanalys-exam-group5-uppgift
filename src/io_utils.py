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
import os

def load_data(file_path: str = "data/ecommerce_sales.csv") -> pd.DataFrame:
    """
    Laddar e-handelsdatan från en CSV-fil till en Pandas DataFrame.
    Konverterar 'date' till datetime och säkerställer korrekta datatyper för numeriska fält.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Hittade inte filen på sökvägen: {file_path}")
    
    # Läs in CSV-filen
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

if __name__ == "__main__":
    # Testkörning för att verifiera inläsning och datatyper
    df = load_data()
    print("Datat har laddats och rensats framgångsrikt!\n")
    print("Datatyper:")
    print(df.dtypes)
    print("\nFörsta raderna:")
    print(df.head())
