# coding=utf-8
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property  # age就是一个只读属性
    def age(self):
        return 2017 - self._birth

s = Student()
s.birth = 1994
print s.age
