
def compute_sum_to_n(n):
    '''
    :param n: input integer n
    :return:  the sum of all non-negative integers up to and including a specified value, n
    '''
    assert isinstance(n, int)
    assert n >= 0
    sum = 0
    for i in range(int(n) +1):
        sum += i
    return sum

