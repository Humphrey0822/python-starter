# coding=utf-8
"""
获取对象信息
"""
"""使用type()"""
print type(123)
print type('str')
print type(None)

import types

print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
"""所有类型本身的类型就是TypeType"""
print type(int)==type(str)==types.TypeType

"""使用isinstance()
能用type()判断的基本类型也可以用isinstance()判断
"""
print isinstance('a', str)
print isinstance(u'a', unicode)
print isinstance('a', unicode)
# 由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
print isinstance(u'a', basestring)

"""使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
"""
print dir('ABC')


# class MyObject(object):
#     def __len__(self):
#         return 100
#
# obj = MyObject()
# print len(obj)

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

object = MyObject()
print object.x
print object.power()