from collections import Counter
def threshold_values(seq,threshold=1):
    '''
    :param seq: sequence list
    :param threshold: threshold of string
    :return: dict
    '''
    assert isinstance(seq, list)
    for s in seq:
        assert isinstance(s, str)
    assert isinstance(threshold, int)
    assert threshold > 0
    cnt = Counter(seq)
    assert threshold <= len(cnt.keys())
    temp = sorted(cnt)
    dic = dict()
    dic_num = dict()
    for s in seq:
        dic[s] = []
    for s in seq:
        if s.count('0') <= s.count('1'):
            dic_num[s] = cnt[s]
    dic_num = sorted(dic_num.items(),key = lambda item: item[1],reverse = True)
    res = dict(dic_num[:threshold])
    print(res)
    for s in seq:
        if s.count('0') > s.count('1'):
            dic[s] = 0
        else:
            if s in res.keys():
                dic[s] = 1
            else:
                dic[s] = 0
    return dic

# seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
# x=['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
# print(threshold_values(x,2))