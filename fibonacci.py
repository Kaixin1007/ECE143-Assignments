def fibonacci(n):
    '''
    Write a generator to compute the first n Fibonacci numbers
    :param n: Fibonacci numbers
    :return: null
    '''
    assert isinstance(n, int)
    assert n >=0
    i = 0
    x = 0
    y = 1
    while i < n:
        yield y
        tmp = y
        y = x +y
        x = tmp
        i = i+1


