# coding=utf-8
test1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# 用For循环遍历列表，没有循环变量，更加简洁
for i in test1:
    print i
# 1.打印0-19之间所有奇数
test2 = range(20)
for i in test2:
    if i % 2:
        print i
