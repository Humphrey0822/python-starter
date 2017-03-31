# coding=utf-8
"""
   修饰器有参数：
   a. 被修饰对象无参数
"""


def test(printResult=False):
    def _test(func):
        def __test():
            print 'Call the function %s().' % func.func_name
            if printResult:
                print func()
            else:
                return func()
        return __test
    return _test


@test()
def say():
    return 'hello world'

# say()

"""
    当装饰器有参数时，即使你启用装饰器的默认参数，不另外传递新值进去，
    也必须有一对括号，否则编译器会直接将func传递给test()，而不是传递给_test()
"""

"""b.被修饰对象有参数"""


def test2(printResult=False):
    def _test(func):
        def __test(*args, **kw):
            print 'Call the function %s().' % func.func_name
            if printResult:
                print func(*args, **kw)
            else:
                return func(*args, **kw)
        return __test
    return _test


@test2(printResult=True)
def left(Str, Len):
    # The parameters of __test can be '(Str, Len)' in this case.
    return Str[:Len]


left('hello world', 5)







