from time import sleep
import random
from datetime import datetime
import itertools as it
from types import GeneratorType
def tracker(p,limit=3):
    '''
    :param p: producer
    :param limit:  the number of odd-numbered seconds to track until completion
    :return: the number of odd numbered seconds that have been iterated over
    '''
    assert isinstance(p, GeneratorType)
    assert isinstance(limit, int)
    assert limit > 0

    count = 0
    while(count < limit):
        sec = next(p).seconds
        if int(sec) % 2  == 1:
            count = count +1
        newLimit = yield count
        if newLimit:
            limit = newLimit


# def producer():
#     'produce timestamps'
#     starttime = datetime.now()
#     while True:
#         sleep(random.uniform(0,0.2))
#         yield datetime.now()-starttime
# p = producer()
# t = tracker(p,limit=3)
# print(next(t))
# print(next(t))
# t.send(5)
# print(list(t))
