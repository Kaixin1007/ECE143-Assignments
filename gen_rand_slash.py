import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def gen_rand_slash(m=6,n=6,direction='back'):
    '''

    :param m: The m is the number of rows in the image
    :param n:The n is the number of column in the image
    :param direction: back or forward
    :return: can produce a uniformly random forward or backslashed image (i.e., Numpy array) of at least two non-zero pixels
    '''

    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(direction, str)
    assert n > 1 and m > 1
    assert direction == 'back' or direction == 'forward'
    res = np.zeros((m,n))

    if(direction == 'forward'):
        row = random.choice(range(m - 1))
        col = random.choice(range(1, n))
        len = random.choice(range(2,min(m,n)+1))
        for i in range(len):
            if row <0 or col < 0 or row >= m or col >=n:
                break
            res[row][col] = 1
            row +=1
            col -=1
    else:
        row = random.choice(range(m - 1))
        col = random.choice(range(n - 1))
        len = random.choice(range(2, min(m,n)+1))
        for i in range(len):
            if row <0 or col < 0 or row >= m or col >=n:
                break
            res[row][col] = 1
            row +=1
            col +=1

    return res

fig,axs=plt.subplots(3,3,sharex=True,sharey=True)
for ax in axs.flatten():
    ax.imshow(gen_rand_slash(direction ='forward'), cmap=cm.gray_r)


    # for ax in axs.flatten():
    #
plt.show()