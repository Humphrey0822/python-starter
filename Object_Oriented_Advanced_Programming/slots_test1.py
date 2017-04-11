# coding=utf-8
class Student(object):
    pass

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print s.name


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)
print s.age

s2 = Student()
# s2.set_age(25)


def set_score(self, score):
    self.score = score

# 给class绑定方法
Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
print s.score
s2.set_score(99)
print s2.score