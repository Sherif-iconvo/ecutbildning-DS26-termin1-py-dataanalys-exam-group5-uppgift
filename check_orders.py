# Hämta Sfunktion för att läsa rådata.
from src.io_utils import load_raw_transactions

# Kör funktionen och spara tabellen i df.
df = load_raw_transactions()

# len(df) räknar alla rader. print visar resultatet.
print("Antal rader:", len(df))

# Välj order_id och räkna hur många olika ID som finns.
print("Unika order-ID:", df["order_id"].nunique())

# Resultat: 2 500 rader och 2 500 unika order-ID.
# Inga order-ID återkommer.
# Gruppering per order-ID ger därför en rad per grupp.