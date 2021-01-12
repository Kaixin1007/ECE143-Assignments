import numpy as np
from itertools import combinations
def get_min_split(seq):
    '''
    :param seq:a Python list or 1-dimensional Numpy array
    :return:the absolute difference between the respective sums of the subsets is as small as possible
    '''
    assert isinstance(seq, (list, np.ndarray))
    minVal = 10000000
    size = int(len(seq)/2)
    for i in range(1,size+1):
        for c in combinations(seq, i):
            retD = list(set(seq).difference(set(c)))
            dif = abs(sum(retD)-sum(c))
            minVal = min(dif,minVal)

    res = []
    temp = set()
    for i in range(1,size+1):
        for c in combinations(seq, i):
            if(tuple(c) not in temp):

                retD = list(set(seq).difference(set(c)))
                dif = abs(sum(retD) - sum(c))
                retD.sort()

                temp.add(tuple(retD))
                c = list(c)
                c.sort()
                if minVal == dif:
                    res.append((retD,c))
    return res


#
seq = [5,10, 15,20,25,30]
print(get_min_split(seq))
