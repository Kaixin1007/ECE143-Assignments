import itertools


def get_power_of3(val):
    '''
    :param val: input number
    :return: list result
    '''
    assert isinstance(val,int)
    assert val >=1 and val <= 40
    for i in itertools.product([-1, 0, 1],[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]):
        if i[0] + i[1]*3 + i[2] * 9 + i[3] * 27 == val:
            return list(i)

