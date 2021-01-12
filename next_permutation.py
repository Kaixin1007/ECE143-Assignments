def Reverse(nums, start, end):
    '''
    reverse helper function
    '''
    mid = (start + end + 1) // 2
    k = 0
    for j in range(start, mid):
        nums[j], nums[end - k] = nums[end - k], nums[j]
        k += 1
def next_permutation(t:tuple)->tuple:
    '''
    :param t: input
    :return: next permutation in lexicographic order
    '''
    assert isinstance(t, tuple)
    assert len(t)> 0
    t = list(t)

    for i in t:
        assert isinstance(i, int)
        assert i >= 0
    temp = set(t)
    assert len(temp) == len(t)
    index = 0
    for i in range(len(t) - 1, 0, -1):
        if t[i] > t[i - 1]:
            index = i
            break
    if index == len(t) - 1:
        t[index], t[index - 1] = t[index - 1], t[index]
    elif index == 0:
        Reverse(t, 0, len(t) - 1)
    else:
        Reverse(t, index, len(t) - 1)
        for s in range(index, len(t)):
            if t[s] > t[index - 1]:
                t[index - 1], t[s] = t[s], t[index - 1]
                break
    return tuple(t)

# print(next_permutation((0, 5, 2, 1, 4, 7, 3, 6)))

