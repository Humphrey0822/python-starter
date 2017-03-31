# coding=utf-8
import re
"""
   修饰类：被修饰的对象时一个类
"""


# a. 被修饰对象无参数
# def test(cls):
#     def _test():
#         clsName = re.findall('(\w+)', repr(cls))[-1]
#         print 'Call %s.__init().' % clsName
#         return cls()
#     return _test
#
#
# @test
# class sy(object):
#     value = 32

# s = sy()
# print s
# print s.value


# b. 被装饰对象有参数
def test2(cls):
    def _test(*args, **kw):
        clsName = re.findall('(\w+)', repr(cls))[-1]
        print 'Call %s.__init().' % clsName
        return cls(*args, **kw)
    return _test


@test2
class sy2(object):
    def __int__(self, value):
        # The parameters of _test can be '(value)' in this case.
        self.value = value


s = sy2('hello world')


