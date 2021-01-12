def map_bitstring(x):
    '''
    :param x: a list of bitstrings
    :return:maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1
    '''
    assert isinstance(x,list)
    for t in x:
        assert isinstance(t,str)

    dic = dict()
    for s in x:
        if s.count('0') > s.count('1'):
            dic[s] = 0
        else:
            dic[s] = 1
    return dic

# x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
# print(map_bitstring(x))