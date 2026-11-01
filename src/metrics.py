def order_values(df):
    """Beräkna totalt ordervärde per order."""

    # Samla rader med samma order-ID och summera intäkten.
    order_total = df.groupby("order_id")["revenue"].sum()

    # Lämna tillbaka ordervärdena.
    return order_total