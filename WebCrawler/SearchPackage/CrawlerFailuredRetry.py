# coding=utf-8
from requests.exceptions import ConnectTimeout
import requests
from retry import retry


# 第一种方法
def do_some(url, n=1):
    # 给n一个默认值1
    print n,url
    if n > 2:
        print 'retry many times'
        return None
    try:
        r = requests.get(url, timeout=2)
        return r.text
    except Exception as e:
        print e.args
        n += 1
        # 失败 n加一，重试
        return do_some(url, n)


# 第二种方法：采用retry模块
@retry(exceptions=ConnectTimeout, tries=3)
# tries=3 表示重试次数，该注解采用装饰器设计
def do_other(ourl):
    print ourl, 'ddddddddd'
    r = requests.get(ourl, timeout=1)
    return r.text


if __name__ == '__main__':
    ourl = 'https://www.google.com'
    # 方法1
    # do_some(ourl)

    try:
        do_other(ourl)
    except Exception as e:
        print 'dsssssssss'
        pass

