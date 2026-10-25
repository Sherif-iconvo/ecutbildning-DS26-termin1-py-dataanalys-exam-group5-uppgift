import pandas as pd


class EcommerceAnalyzer:
    """
    Klass för analys av e-handelsdata.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_total_revenue(self) -> float:
        """
        Calculate and return the total revenue.
        """
        return self.df["revenue"].sum()


if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    analyzer = EcommerceAnalyzer(df)

    print("Total revenue:")
    print(analyzer.get_total_revenue())