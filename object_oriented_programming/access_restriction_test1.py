# coding=utf-8
# 访问限制-封装


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
print bart._Student__name
"""
Traceback (most recent call last):
  File "D:/PythonDevelop/PycharmProjects/python-starter/object_oriented_programming/access_restriction_test1.py", line 10, in <module>
    print bart.__name
AttributeError: 'Student' object has no attribute '__name'
"""
print bart.set_score(90)
"""
Traceback (most recent call last):
  File "D:/PythonDevelop/PycharmProjects/python-starter/object_oriented_programming/access_restriction_test1.py", line 29, in <module>
    print bart.set_score(121)
  File "D:/PythonDevelop/PycharmProjects/python-starter/object_oriented_programming/access_restriction_test1.py", line 19, in set_score
    raise ValueError('bad score')
ValueError: bad score
"""
