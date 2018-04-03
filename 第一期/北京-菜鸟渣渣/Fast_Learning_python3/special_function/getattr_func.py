#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")



class A:
    def __init__(self):
        self.name = 'zhangjing'
        # self.age='24'
    def method11(self):
        print
        "method print"

Instance = A()
#如果Instance 对象中有属性name则打印self.name的值，否则打印not find
print (getattr(Instance , 'name','123' ))
print (getattr(Instance, 'method1', 'default'))


class test:
    pass


o = test()
print(str(o))