#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


class Person(object):
    """Silly Person"""

    def __new__(cls, name, age):
        print('__new__ called.')
        print(name)
        print(age)
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age
        print("12321")

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)


if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print(piglei)
