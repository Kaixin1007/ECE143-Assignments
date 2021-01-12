import random
def get_sample(nbits=3,prob=None,n=1):
    '''
    :param nbits: number of bits
    :param prob: corresponding dictionary
    :param n: number of random samples
    :return: result
    '''
    assert isinstance(nbits, int)
    assert isinstance(n, int)
    assert isinstance(prob, dict)
    assert nbits >0 and n > 0
    assert (0 <= x <= 1 for x in prob.values())
    assert(sum(list(prob.values())) == 1)
    assert (len(y) == nbits for y in prob.keys())
    assert len(list(prob.keys())) == 2 ** nbits
    res = random.choices(list(prob.keys()),list(prob.values()),k=n)
    return list(res)




