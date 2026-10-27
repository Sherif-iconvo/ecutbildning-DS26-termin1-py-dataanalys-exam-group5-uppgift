import pandas as pd

#Loading data and do a parse change.
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df

def data_check(df):
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
    #Giving us a final information about our columns.
    print(df.info())   
    print(df.describe())