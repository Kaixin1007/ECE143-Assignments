def slide_window(x,width,increment):
    '''
    Implement a sliding window for an arbitrary input list
    :param x: input list
    :param width: window width
    :param increment: window increment
    :return:  res
    '''
    assert isinstance(x, list)
    assert isinstance(width, int)
    assert isinstance(increment, int)
    assert width > 0 and width <= len(x)
    assert increment>0
    res = []
    for i in range(0,len(x),increment):
        if i <= len(x)-width:
            res.append(x[i:i+width])

    return res

print(slide_window(list(range(18)),5,2))