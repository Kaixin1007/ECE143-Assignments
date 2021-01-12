import numpy as np
def solvefrob(coefs,b):
    '''
    :param coefs: the list of a_i coefficients
    :param b: value
    :return:
    '''
    assert isinstance(coefs, list)
    assert isinstance(b, int)
    assert b > 0
    for i in coefs:
        assert i > 0
    coefs = np.array(coefs)
    b = np.array(b)
    max_val = b/coefs
    max_val = max_val.astype(int)

    x_potential = []
    for i in range(coefs.shape[0]):
        arr = np.arange(max_val[i] + 1) * np.array([coefs[i]])
        x_potential.append(arr)

    sum = 0
    for i in range(coefs.shape[0]):
        res = []
        for j in range(coefs.shape[0]):
            if j == i:
                res.append(max_val[i] + 1)
            else:
                res.append(1)
        sum = sum + x_potential[i].reshape(tuple(res))
        # print(sum)
        # print("-------------")
    res = []
    for i in np.array(np.where(sum == b)).T:
        res.append(tuple(i))
    return res


# print(solvefrob([1,2,3,5],10))


