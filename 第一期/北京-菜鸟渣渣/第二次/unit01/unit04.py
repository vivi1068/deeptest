# -*- coding:utf-8 -*-
__author__ = 'Young'
# _单下划线开头 只有子类或者类内部才可以访问,
# __ 双下划线开头只有  类内部可以访问
class MyClass():
    __age = 21

    def __init__(self, name=None):
        self.__name = name

    def func(self, age):
        return "Name: %s, Age: %s" % (self.__name, age)


mc = MyClass('xiaoming')
print mc.func('22')
# print mc.__name
# print mc.__age

class MyClass():
    '''
    THIS IS A CLASS Entity
    '''
    __age = 21

    def __init__(self, name=None):
        self.__name = name

    def func(self, age):
        # print self.__str__()
        return "Name: %s, Age: %s" % (self.__name, age)


print MyClass.__doc__
print dir(MyClass)


class Parent():
    __PI = 14.25

    def __init__(self, name=None):
        self._name = name
        print Parent.__PI
        print self.__PI

    def func(self, age):
        return "Name: %s, Age: %s" % (self._name, age)


class Child(Parent):
    pass


mc = Child('yangying')
print mc.func(25)
print mc._name

class A:
    def __call__(self,x):
        print "call........"
        print  x
c=A()
c(2500)

class AA:
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
aa=AA()
aa(1,2,3,a=1,b=2,c=55)



"""Force name to be global in scope.

        Some child of the current node had a free reference to name.
        When the child was processed, it was labelled a free
        variable.  Now that all its enclosing scope have been
        processed, the name is known to be a global or builtin.  So
        walk back down the child chain and set the name to be global
        rather than free.

        Be careful to stop if a child does not think the name is
        free.
"""
Object = object


class Parent1(Object):
    _Parent = "fault"

    def __init__(self):
        self.name_a = "xiaoming"

    def _funcA(self, age):
        print  "function A: %s,%d" % (self.name_a, age)


class Child(Parent1):
    _pNum=100
    def __init__(self,age):
        # Parent1.__init__(self)
        super(Child, self).__init__()
        self.name_b = "zhangsan"
        self.age=age
        print self.age

    def funcA(self, age):
        print "before"
        # Parent1._funcA(self,age)
        super(Child, self)._funcA(age)
        print "After"

mess = Child(150)

print "------------->",getattr(mess,'_pNum',None)
setattr(mess,'age',151)
delattr(mess,"age")
print hasattr(mess,"age")
# print mess.age
# mess.funcA(150)
