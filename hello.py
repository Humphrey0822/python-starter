# coding=utf-8
"""a test module, name of module is hello"""


__author__ = 'Humphrey Sun'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'


if __name__ == '__main__':
    test()
    try:
        # cString是C写的，速度更快
        import cStringIO as StringIO  # 别名
    except ImportError:  # 导入失败会捕获到ImportError
        import StringIO

    try:
        import json  # python >= 2.6
    except ImportError:
        import simplejson as json  # python <= 2.5版本是单独的第三方库，2.6开始内置


# _xxx和__xxx这样的函数或变量就是非公开的(private),不应该被直接引用
def _private_1(name):
    return "Hello, %s" % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
