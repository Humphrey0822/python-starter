import re

text = "JGood is a handsome boy, he is coll, clever, and so on..."
m = re.match(r"(\w+)\s", text)
if m:
    print m.group(0), '\n', m.group(1)
else:
    print 'not match'

print 't\rd'

print 'PROBLEM\r\nP1\r\nEndpoint: localhost\r\nMetric: cpu.user\r\nTags: \r\nall(#3): 1.00503!=0\r\nNote: \xe6\xb5\x8b\xe8\xaf\x95-\xe6\x8a\xa5\xe8\xad\xa6\xe5\x90\x88\xe5\xb9\xb6-p1\r\nMax: 3,Current: 1\r\nTimestamp: 2016-11-2815: 33: 00\r\nhttp: //10.70.82.59: 5050/template/view/8\r\n'
