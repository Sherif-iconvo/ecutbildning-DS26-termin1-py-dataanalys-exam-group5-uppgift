import pandas as pd
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