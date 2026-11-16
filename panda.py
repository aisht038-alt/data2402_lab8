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

def filter_data(df):

    good = df[df['class'] == 'good']
    print(len(good))
    print(good)

    bad = df[df['class'] == 'bad']
    print(len(bad))
    print(bad)

    high_wage = df[df['wage-increase-first-year'] > 2.5]
    print(len(high_wage))
    print(high_wage)

    many_holidays = df[df['statutory-holidays'] > 10]
    print(len(many_holidays))
    print(many_holidays)

    both = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    print(len(both))
    print(both)

    print(df['wage-increase-first-year'].mean())
    print(df['wage-increase-first-year'].max())

def task3_filter_data(df):

    good = df[df['class'] == 'good']
    print(len(good))
    print(good)

    bad = df[df['class'] == 'bad']
    print(len(bad))
    print(bad)

    high_wage = df[df['wage-increase-first-year'] > 2.5]
    print(len(high_wage))
    print(high_wage)

    many_holidays = df[df['statutory-holidays'] > 10]
    print(len(many_holidays))
    print(many_holidays)

    both = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    print(len(both))
    print(both)

    print(df['wage-increase-first-year'].mean())
    print(df['wage-increase-first-year'].max())

def main():

    df = load_explore("labor.csv")
    access_data(df)
    filter_data(df)

main()