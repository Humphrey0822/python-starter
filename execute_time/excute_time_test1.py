import datetime


def time_1():
    begin = datetime.datetime.now()
    sum = 0
    for i in xrange(10000000):
        sum = sum + i
    end = datetime.datetime.now()
    return end - begin


print time_1()

