# coding=utf-8
# 函数len返回列表的长度，即元素的个数
aa = [1, 2, 3, 4, 5]
print 'length of aa is', len(aa)  # result:length of aa is 5
# 可以使用这个值遍历列表的变量，这就意味着，即使列表的长度改变了，我们也不用对程序的
# 循环次数做出修改
# 例如：
i = 0
while i < len(aa):
    print aa[i]
    i += 1
# in是一个布尔操作符，他测试左边的操作数是否包含于列表
if 1 in aa:
    print 'Very Good'
else:
    print 'Not Bad'

bb = '12334'
if '1' in bb:
    print 'Very Good'
else:
    print 'Not Bad'
