import pandas as pd
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

# dff = pd.read_csv('survey_data.csv')
# add_month_yr(dff)
#
# print(count_month_yr(dff))