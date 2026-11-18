import pandas as pd

def load_explore(filename):
    data = pd.read_csv(filename)

    print('Display first 5 rows:')
    print(data.head())
    print()

    print('Display column names, DataFrame dimensions, column data types:') 
    data.info()
    print('Display column names:')
    print(data.columns.tolist())
    print()
    print('Display DataFrame dimnesions:')
    print(f'{data.shape[0]} rows, {data.shape[1]} columns')
    print()
    print('Display column data types:')
    print(data.dtypes)
    print()

    print('Display wage-increase-first-year as a Series:')
    print(data['wage-increase-first-year'])
    print()

    print('Check for NULL:')
    print(data[data.isna().any(axis=1)])

    return data

# How many rows and columns are in the dataset? 57 rows, 17 columns
# What data types are used? float and string
# How are missing values represented? NaN
# What is the difference between a Series and a DataFrame? Series is a 1D labeled array and DataFrame is a 2D array where each column is a Series


def access_data(df):
    wage1 = df['wage-increase-first-year']

    print('Retrieve first value using .iloc[] and .loc[]:')
    first_iloc = wage1.iloc[0]
    first_loc = wage1.loc[0]
    print('.iloc[]:', first_iloc)
    print('.loc[]:', first_loc)
    print()

    print('First five rows using .iloc')
    first5 = wage1.iloc[0:5]
    print(first5)
    print()

    wage2 = df[['wage-increase-first-year','wage-increase-second-year']]

    print('Retrieve a specific value using .loc[]:')
    specific_val_loc = wage2.loc[1, 'wage-increase-second-year']
    print(specific_val_loc)
    print()

    print('Demonstrate selecting multiple rows and columns using both .loc[]:')
    multiple_loc = df.loc[0:2,['wage-increase-first-year','wage-increase-second-year','pension']]
    print(multiple_loc)
    print()
    print('Demonstrate selecting multiple rows and columns using both .iloc[]:')
    multiple_iloc = df.iloc[0:3, [1,2,6]]
    print(multiple_iloc)
    print()

    return {
        'wage': wage1,
        'first_iloc': first_iloc, 
        'first_loc': first_loc,
        'first5': first5,
        'wages': wage2,
        'specific_val': specific_val_loc,
        'multiple_loc': multiple_loc,
        'multiple_iloc': multiple_iloc
    }

# What is the difference between .loc[] and .iloc[]? iloc is positioned based access using integers and loc is label based access using labels
# How do you select multiple rows and columns? using a range like iloc[:,0:3] or passing a list of specific rows and/or columns loc[[0,1], ['col1','col2']]
# What is the difference between selecting one column and multiple columns? one column returns a Series and multiple returns a DataFrame, using [] inside of df[['col]] means keeping DataFrame structure

def filter_data(df):
    clean_class = df['class'].astype('string').str.strip().str.lower()

    print('Select all disputes with a good outcome:')
    good = df[clean_class == 'good']
    print(len(good))
    print()

    print('Select all disputes with a bad outcome:')
    bad = df[clean_class == 'bad']
    print(len(bad))
    print()

    print('Select disputes where wage_increase_first_year > 2.5:')
    wage_increase_greater = df[df['wage-increase-first-year'] > 2.5]
    print(len(wage_increase_greater))
    print()

    print('Select disputes where statutory_holidays > 10:')
    holidays_greater = df[df['statutory-holidays'] > 10]
    print(len(holidays_greater))
    print()

    print('Select disputes satisfying both conditions:')
    both = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    print(len(both))
    print(both[['wage-increase-first-year','statutory-holidays','class']])
    print()

    print('Calculate the average wage_increase_first_year:')
    avg_wage = df['wage-increase-first-year'].mean()
    print(f'{avg_wage:.2f}')
    print()

    print('Calculate the maximum wage_increase_first_year:')
    max_wage = df['wage-increase-first-year'].max()
    print(max_wage)
    print()

    return {
        'good': good,
        'bad': bad,
        'wage_increase_greater': wage_increase_greater, 
        'holidays_greater': holidays_greater,
        'both': both,
        'avg_wage': avg_wage,
        'max_wage': max_wage
    }

# How many disputes have good and bad outcomes? 37 good outcomes, 20 bad outcomes
# How many disputes satisfy both conditions? 28 disputes
# What are the average and maximum first-year wage increases? avg is 3.80 and max is 7.0


def main():
    filename = 'labor.csv'
    data = load_explore(filename)
    access_data(data)
    filter_data(data)


if __name__ == '__main__':
    main()