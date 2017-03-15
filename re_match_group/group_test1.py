# coding=utf-8
import re

a = "123abc456"
print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0)
print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1)
print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2)
print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3)
'''
    1.正则表达式中的三组括号把匹配结果分成三组
    2.没有匹配成功的，re.search()返回None
    3.当然正则表达式中没有括号，group(1)肯定不对了
'''
