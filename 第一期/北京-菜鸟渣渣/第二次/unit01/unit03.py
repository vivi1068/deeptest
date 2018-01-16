# -*- coding:utf-8 -*-
__author__ = 'Young'
def deco(func):
        print "234"
        return func
@deco
def f1():
    print "Hello ${Runable.disabled}"
f1()
class MyClass():
    '''
    Test class    return "Hello %s!" % name
    '''

    x = 100
    def __init__(self):
        self.name ='xiaoMing '
    def func(self, name):
        return "Hello %s!" % name
    def func2(self):
        self.func(" ")
        return self.x
mc = MyClass()
print mc.x
print '类属性引用',MyClass.x
print mc.func("xiaoming")
print mc.func2(),help(MyClass)

def log(arg):
    def deco(func):
        def _deco(*args, **kwargs):
            print "%s - function name: %s" % (arg, func.__name__)
            return func(*args, **kwargs)
        return _deco
    return deco

@log("info")
def f1(a, b):
    print "f1() run."
    print a + b

f1(1,2)

