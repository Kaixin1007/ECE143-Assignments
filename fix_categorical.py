import pandas as pd
from pandas.api.types import CategoricalDtype
def fix_categorical(x):
    '''
    :param x: take the month-yr dataframe column
    :return: the same dataframe with an updated column of CategoricalDtype
    '''
    assert isinstance(x, pd.DataFrame)

    Categorical = CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018', 'Apr-2018', 'Sep-2018', 'Oct-2018', 'Jan-2019']
                                   ,ordered=True)
    x['month-yr'] = x['month-yr'].astype(Categorical)
    return x


def add_month_yr(x):
    '''
    :param x:pd.DataFrame
    :return:the same dataframe with a new month-yr column
    '''
    assert isinstance(x, pd.DataFrame)
    # df = x['Timestamp']

    x['month-yr'] = pd.to_datetime(x['Timestamp'])
    x['month-yr'] = [str(d.strftime('%b-%Y')) for d in x['month-yr']]
    return x

def count_month_yr(x):
    '''
    :param x: x is a pd.DataFrame
    :return: pd.DataFrame
    '''
    assert isinstance(x, pd.DataFrame)
    df = x['month-yr'].value_counts()
    df = df.to_frame()
    df.rename(columns={'month-yr': 'Timestamp'}, inplace=True)
    df.index.name = 'month-yr'

    return df

dff = pd.read_csv('survey_data.csv')
dd = add_month_yr(dff)
df = dd.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()
print(fix_categorical(dd))