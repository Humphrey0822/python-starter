# coding=utf-8
f = open('/Users/michael/test/txt', 'r')
f.read()
f.close()

try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()

with open('/path/to/file', 'r') as f:
    print f.read()

"""
如果文件很小，read()一次性读取最方便；
如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便：
"""
for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'删掉

