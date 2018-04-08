'''
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print('--%s正在吃东西--'%self.name)

def run(self):
    print('--%s正在跑步--'%self.name)

p=Person('小米',20)
p.eat()
p1=Person('小美',30)


import types
Person.run=types.MethodType(run,Person)#给types.MethodType传入函数名和类名
p.run()
p1.run()
'''
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print('--%s正在吃东西--'%self.name)

def run(self):
    print('--%s正在跑步--'%self.name)

p=Person('小米',20)
p.eat()

import types
p.run=types.MethodType(run,p)#给types.MethodType传入函数名和实例对象
p.run()
