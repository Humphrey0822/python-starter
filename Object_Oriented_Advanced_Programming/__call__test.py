# coding=utf-8
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

"""判断一个对象是否是“可调用”对象"""
print callable(Student('Humphrey'))
print callable(Student)
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')