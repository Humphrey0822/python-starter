#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 爬虫搜房网 房产信息
import requests
from bs4 import BeautifulSoup

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/62.0.3202.62 Safari/537.36'
    }


def get_urls(url):
    html = requests.get(url, headers=headers).text
    table = BeautifulSoup(html, 'lxml').find('div', class_='houseList').find_all('')
    urls = []
    for item in table:
        urls.append(item.find('dl', class_='plotListwrap clearfix').find('a').get('href'))
    return urls


def get_content(url):
    html = requests.get(url, headers=headers,timeout=30).text
    return None


def main():
    start_url = ''
    urls = get_urls(start_url)
    for url in urls:
        get_content(url)


if __name__ == '__main__':
    main()