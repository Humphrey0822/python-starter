# coding=utf-8
class Animal(object):
    pass


# 大类：
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixin(object):
    def run(self):
        print 'Running...'


class FlyableMixin(object):
    def fly(self):
        print 'Flying...'


class CarnivorousMixin(object):
    pass


class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    pass


class Bat(Mammal, FlyableMixin):
    pass

