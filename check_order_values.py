# Hämta Sherifs inläsning och din funktion för ordervärden.
from src.io_utils import load_and_clean_transactions

# Hämta orderfunktionen från din egen AOV-fil.
from aov_issue41 import order_values

# Läs in och rensa datan.
df = load_and_clean_transactions()

# Beräkna totalt ordervärde per order.
ordervarden = order_values(df)

# Visa de fem första ordervärdena.
print(ordervarden.head())

# Summera intäkten före och efter grupperingen.
print("Intäkt före gruppering:", round(df["revenue"].sum(), 2))
print("Intäkt efter gruppering:", round(ordervarden.sum(), 2))

# Jämför antal unika order-ID med antal beräknade ordervärden.
print("Unika order-ID:", df["order_id"].nunique())
print("Antal ordervärden:", len(ordervarden))

# Kontroll för issue #38:
# Funktionen ger 2 500 ordervärden för 2 500 unika order-ID.
# Total intäkt före och efter gruppering är 3 502 767,23.
# Grupperingen bevarar alltså den totala intäkten.