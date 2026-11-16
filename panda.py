import pandas as pd

def load_explore():

    df = pd.read_csv("labor.csv")
    print(df.head())
    print(df.columns)
    print(df.shape)
    print(df.dtypes)
    print(df['wage-increase-first-year'])

    return df

def access_data(df):

    load_explore()
    series = df['wage-increase-first-year']
    print(series.iloc[0])
    print(series.loc['2'])
    print(series.iloc[0:5])

    two_columns = df[['wage-increase-first-year', 'wage-increase-second-year']]
    print(two_columns.loc['5'])
    print(df.iloc[[0, 3, 5]])
    print(df.loc[['1', '4', '6']])

access_data()