# coding=utf-8
"""
    修饰器无参数
    b. 被修饰对象有参数
"""


def test(func):
    def _test(*args, **kw):
        print 'Call the function %s().' % func.func_name
        return func(*args, **kw)
    return _test


@test
def left(Str, Len):
    # The parameter of _test can be '(Str, Len)' in this case
    print Str[:Len]


left('hello world', 5)



