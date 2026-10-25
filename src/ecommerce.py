import pandas as pd


class EcommerceAnalyzer:
    """
    Klass för analys av e-handelsdata.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df


if __name__ == "__main__":
    from io_utils import load_data

    df = load_data()

    analyzer = EcommerceAnalyzer(df)

    print("EcommerceAnalyzer created successfully.")