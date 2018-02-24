# coding=utf-8
import json, requests


def search_package():
    # 输入运单号码，注意，只有正在途中的快递才可以查到！
    packageNum = input('请输入运单号码：')
    url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + str(packageNum)
    # {"comCode":"","num":"888292558660606106","auto":[{"comCode":"yuantong","id":"","noCount":993903,"noPre":"88829","startTime":""}]}
    companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
    # url2 = 'http://cache.kuaidi100.com/index.html?option=add&gCompanyCode=' + companyName + '&gKuaidiNumber=' + packageNum + '&gIsCheck=0'
    url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + str(packageNum) +'&temp=0.10246537271755507'
    print ('时间↓                 地点和跟踪进度↓\n')
    for item in json.loads(requests.get(url2).text)['data']:
        print item['time'],item['context']

search_package()