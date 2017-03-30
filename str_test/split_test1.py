# coding=utf-8


def split_print(text):
    s = text.split(" ")

    print 'n=', len(s)
    for i in range(0, len(s)):
        if s[i] == '':
            print str(i)+':为空字符串'
        else:
            print str(i)+':'+s[i]

text = "年老代的内存使用率 all(#3) old.gen.mem.ratio jmxport=8999 26.93>90"
text1 = "购物车模块10.70.14.72:8080连接时长（大于500ms,且持续3分钟警告） all(#3) cart_ng.hc.timing/server=10.70.14.72_8080.col  40431>500"
text2 = "磁盘读速度 /秒 超过1000且持续时间超过10分钟报警 all(#10) disk.io.msec_read device=sdb 945.35>1000"
# split_print(text2)
# print "============="
# split_print(text1)


def get_full_metric(msg):
    s = msg.split(" ")
    n = len(s)
    if s[n-2] == '':
        full_metric = s[n-3]
    else:
        full_metric = s[n-3] + '/' + s[n-2]
    return full_metric.strip()


print get_full_metric(text1)