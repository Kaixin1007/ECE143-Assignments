import pandas as pd
def split_count(x):
    '''
    :param x: is a pd.Series object
    :return: pd.DataFrame object.
    '''

    assert isinstance(x, pd.Series)
    temp = x.str.split(', ')

    df_temp = pd.DataFrame(columns=('idx',))

    for i in range(temp.shape[0]):
        for j in range(len(temp[i])):
            df_temp = df_temp.append(pd.DataFrame({'idx':[temp[i][j]]}),ignore_index=True)
            # print(temp[i][j])
            # df.insert(temp[i][j])

    res = df_temp['idx'].value_counts(ascending=True)
    res = res.to_frame()
    res.rename(columns={'idx': 'count'}, inplace=True)
    return res

df = pd.read_csv('survey_data.csv')
x = df['Is there anything in particular you want to use Python for?']
print(split_count(x))
