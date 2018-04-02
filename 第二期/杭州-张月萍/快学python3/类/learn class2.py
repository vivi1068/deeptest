# -*- coding: utf-8 -*-
# __author__ = 'Carina'

# 实例属性如被重新赋值，不会影响到类属性的引用
class TestA():
    attr1 = 2
obj_a1 = TestA()
obj_a2 = TestA()

obj_a1.attr1 = 43
print(obj_a1.attr1)
print(obj_a2.attr1)
print(TestA.__dict__)   # 类的特殊属性，用于储存类或者实例的属性，默认隐藏


# 类属性被重新赋值,会影响类属性的引用
class TestB():
    attr = 1
obj_b1 = TestB()
TestB.attr = 42
print(obj_b1.attr)
print(TestB.__dict__)
print(obj_b1.__dict__)


# 类属性、实例属性具有相同的名称
class TestC():
    attr = 3
    def __init__(self):
        self.attr = 45

obj_c1 = TestC()
print(obj_c1.attr)


# 类的扩展理解，内建类型
obj11 = 1
obj12 ='string'
obj13 = []
obj14 ={}
print(type(obj11),type(obj12),type(obj13),type(obj14))
