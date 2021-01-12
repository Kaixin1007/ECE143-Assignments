import pandas as pd
def add_month_yr(x):
    '''
    :param x:pd.DataFrame
    :return:the same dataframe with a new month-yr column
    '''
    assert isinstance(x, pd.DataFrame)
    # df = x['Timestamp']

    # x['month-yr'] = pd.to_datetime(x['Timestamp'])
    x['month-yr'] = [str(d.strftime('%b-%Y')) for d in pd.to_datetime(x['Timestamp'])]

    return x



#
dff = pd.read_csv('survey_data.csv')
print(add_month_yr(dff)['month-yr'])
