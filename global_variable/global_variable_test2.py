# coding=utf-8
"""
    全局变量第二种使用方式：
    是在一个单独的模块中定义好，然后在需要使用的全局模块中将定义的全局变量模块导入
"""
import global_list


def tt():
    print global_list.GLOBAL_A

if __name__ == '__main__':
    tt()