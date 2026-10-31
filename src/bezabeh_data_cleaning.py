# Hämta pandas för att arbeta med tabeller.
import pandas as pd


def load_and_clean_data(file_path):
    """Läs CSV-filen och omvandla datumkolumnen."""

    # Läs filen från sökvägen som funktionen får.
    data = pd.read_csv(file_path)

    # Omvandla text till datum. Stoppa vid ogiltiga datum.
    data["date"] = pd.to_datetime(data["date"], errors="raise")

    # Lämna tillbaka tabellen.
    return data

# en funktion som sammanfattar datakvaliteten.

def check_data_quality(data):
    """Visa tabellens storlek och antal saknade värden."""

    # Visa antal rader och kolumner.
    print("Rader och kolumner:", data.shape)

    # Räkna saknade värden i varje kolumn.
    print("Saknade värden per kolumn:")
    print(data.isna().sum())


            # Räkna exakt upprepade rader i hela tabellen.
    print("Exakt upprepade rader:", data.duplicated().sum())

    # Räkna extra förekomster av samma order-ID.
    print("Återkommande order-ID:", data["order_id"].duplicated().sum())

        # Räkna rader per stad, inklusive eventuella saknade värden.
    print("Rader per stad:")
    print(data["city"].value_counts(dropna=False))

    # Räkna rader per kategori, inklusive eventuella saknade värden.
    print("Rader per kategori:")
    print(data["category"].value_counts(dropna=False))

    # kontrollen att intäkt stämmer med pris gånger antal.
        # Beräkna pris gånger antal, avrundat till två decimaler.
    beraknad_intakt = (data["price"] * data["units"]).round(2)

    # Beräkna skillnadens storlek.
    skillnad = (data["revenue"] - beraknad_intakt).abs()

    # Räkna skillnader som är större än 0,01.
    print("Intäktsavvikelser större än 0,01:", (skillnad > 0.01).sum())
        # Visa de fem raderna med högst intäkt.
    print("Fem rader med högst intäkt:")
    print(data.nlargest(5, "revenue"))

if __name__ == "__main__":
    # Hitta projektmappen.
    from pathlib import Path
    projektmapp = Path(__file__).resolve().parent.parent

    # Hitta CSV-filen.
    filsokvag = projektmapp / "data" / "ecommerce_sales.csv"

    # Läs in datan och kör kontrollerna.
    data = load_and_clean_data(filsokvag)
    check_data_quality(data)
    print("Återkommande order-ID:", data["order_id"].duplicated().sum())