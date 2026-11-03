# Hämta Sherifs funktion

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

def sales_totals(df):
    """Beräkna totalt antal sålda enheter och total intäkt."""

    total_units = df["units"].sum()
    total_revenue = df["revenue"].sum()

    return total_units, total_revenue


def order_value_spread(df):
    """Visa hur ordervärdena varierar."""

    orders = order_values(df)
    return orders.describe()


if __name__ == "__main__":
    # Läs datan med Sherifs funktion.
    df = load_and_clean_transactions()

    # Kör beräkningarna.
    aov, antal_order, antal_enheter = aov_and_units(df)
    enheter, intakt = sales_totals(df)
    spridning = order_value_spread(df)

    # Visa resultaten.
    print("AOV:", round(aov, 2))
    print("Antal order:", antal_order)
    print("Sålda enheter:", enheter)
    print("Total intäkt:", round(intakt, 2))
    print("Spridning för ordervärden:")
    print(spridning)