#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 21:08
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson10.py
# @Software: PyCharm
class DemoClass(object):

    def __init__(self):
        print("我是初始化")

    def output(self, text):
        print("输出 %s" %text)

    def output_none(self):
        print("我是不能传入参数的")

class ChildDemoClass(DemoClass):

    def __init__(self):
        print("我是子类")

    def output_none(self):
        print(u"我是子类不能传参的方法")

if __name__ == "__main__":
    #类的实例化是对象

    #创建一个类对象
    demo = DemoClass()
    #调用output
    demo.output("我是文本")
    #调用output_none
    demo.output_none()
    print("--------------------------------")

    #创建子类的对像
    child_demo = ChildDemoClass()
    #调用output,调用的是父类的方法
    child_demo.output("我是子类中调用父类的方法")
    #调用output_nome,调用的是子类的方法，即重写过的方法
    child_demo.output_none()
