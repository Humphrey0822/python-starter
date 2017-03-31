# coding=utf-8
"""
    修饰器无参数
    a. 被修饰对象无参数
"""


def test(func):
    def _test():
        print 'Call the function %s().' % func.func_name
        return func()
    return _test


@test
def say():
    print 'hello world'

say()


