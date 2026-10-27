import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def data_check(df):
    #We want to check if out data is good to use:

    #Checks wheter there is any missing values.
    missing_values = df.isna().sum().sum()
    if missing_values > 0:
        print("We have this many missing values: ", missing_values)
    else:
        print("We have no missing values.")

    #Checks wheter there is any duplicated rows.
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print("We have this many duplicates: ", duplicates)
    else:
        print("No duplicates in the file was found.")