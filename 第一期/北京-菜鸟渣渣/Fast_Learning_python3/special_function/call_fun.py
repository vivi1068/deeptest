#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def  __call__(self, name):
        print("myfried%s"%(name))



p = Person('Bob', 'male')
Person("BOB")
