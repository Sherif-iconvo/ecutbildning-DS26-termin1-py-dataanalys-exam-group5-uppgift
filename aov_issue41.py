from src.io_utils import load_and_clean_transactions
from src.metrics import order_values


def aov_and_units(df):
    """Beräkna AOV, antal order och totalt antal enheter."""

    # Hämta ordervärden och räkna order.
    orders = order_values(df)
    order_count = len(orders)

    # Undvik division med noll.
    if order_count == 0:
        raise ValueError("Kan inte beräkna AOV utan order.")

    # Beräkna genomsnittligt ordervärde och antal enheter.
    aov = orders.sum() / order_count
    total_units = df["units"].sum()

    return aov, order_count, total_units


if __name__ == "__main__":
    # Läs datan och kör funktionen.
    df = load_and_clean_transactions()
    aov, antal_order, antal_enheter = aov_and_units(df)

    # Skriv ut resultaten.
    print("AOV:", round(aov, 2))
    print("Antal order:", antal_order)
    print("Totalt antal enheter:", antal_enheter)