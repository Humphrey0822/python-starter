# coding=utf-8
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    def __iter__(self):
        return self  # 实例本身就是迭代兑现个，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a  # 返回下一个值

for n in Fib():
    print n