import random
def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''
    assert isinstance(n, int)
    assert isinstance(p, list)
    assert isinstance(k, int)
    assert k > 0 and n > 0
    assert sum(p) == 1
    temp = range(0,len(p))
    ans = []
    for i in range(k):
        sample = random.choices(temp, p, k = n)
        freq = [0] * len(p)
        for j in sample:
            freq[j] += 1

        ans.append(freq)
    return ans

# print(multinomial_sample(10,[1/3,1/3,1/3],k=10))
