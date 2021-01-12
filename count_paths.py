
def count_paths(m,n,blocks):
    '''
    :param m: rows
    :param n: columns
    :param blocks:  is a list of tuples indicating the blocked # entries in the grid
    :return: the number of connected paths between the top-left square and the bottom right 
    '''
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert m > 0 and n > 0
    assert isinstance(blocks, list)
    for i in blocks:
        assert isinstance(i,tuple)
        assert isinstance(i[0],int)
        assert isinstance(i[1], int)
        assert i[0] >= 0 and i[0] < m
        assert i[1] >= 0 and i[1] < n
    dp = [[0 for j in range(n)] for i in range(m)]
    ob = [[0 for j in range(n)] for i in range(m)]
    for i in blocks:
        ob[i[0]][i[1]] = 1

    for j in range(0, n):
        if ob[0][j] == 0:
            dp[0][j] = 1
        else:
            break
    for i in range(0,m):
        if ob[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    for i in range(1, m):
        for j in range(1, n):
            if(ob[i][j] == 0):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


# print( count_paths(3,4,[(0,3),(1,1)]))
