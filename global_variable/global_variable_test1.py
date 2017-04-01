# coding=utf-8
"""
    全局变量第一种使用方式：
    直接在当前的模块中定义好，然后直接在本模块中通过global声明，然后使用
"""
SOLR_URL='http://solr.org'


def tt():
    global SOLR_URL
    SOLR_URL=SOLR_URL+'#aa'


if __name__ == '__main__':
    tt()
    print SOLR_URL

