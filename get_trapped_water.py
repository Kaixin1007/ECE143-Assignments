def get_trapped_water(seq):
    '''
    :param seq: input list
    :return: how many units of water remain trapped between the walls in the map
    '''
    assert isinstance(seq, list)
    assert len(seq) != 0
    for i in seq:
        assert isinstance(i,int)
        assert i >=0
    n = len(seq)
    left, right = 0, n - 1
    max_left, max_right = seq[0], seq[-1]
    res = 0
    while left <= right:
        max_left = max(seq[left], max_left)
        max_right = max(seq[right],max_right)
        if max_left < max_right:
            res += max_left - seq[left]
            left += 1
        else:
            res += max_right - seq[right]
            right -= 1
    return res

# print(get_trapped_water([3, 0, 1, 3, 0, 5]))
# print(get_trapped_water([]))