
def gather_values(x):
    '''
    :param x: input list of string
    :return:produce the following output from x
    '''
    assert isinstance(x,list)
    for t in x:
        assert isinstance(t,str)
    dic = dict()
    for s in x:
        dic[s] = []
    for s in x:
        if s.count('0') > s.count('1'):
            dic[s].append(0)
        else:
            dic[s].append(1)
    return dic
# x =  ['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
# print(gather_values(x))