#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 18:36
# @Author  : yulu
# @File    : calculator
class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 重置数据
    def set(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def add(self, a, b):
        self.result = self.a + self.b
        print ("和： ", self.result)

    # 减法
    def sub(self, a, b):
        self.result = self.a - self.b
        print("差： ", self.result)

    # 乘法
    def mul(self, a, b):
        self.result = self.a * self.b
        print("积： ", self.result)

    # 除法
    def div(self, a, b):
        if self.b == 0:
            print("除数不能为0")
            return
        else:
            self.result = self.a / self.b
            print("商： ", self.result)

# def test(calc):
#     calc.__init__()
#     calc.add()
#     calc.sub()
#     calc.mul()
#     calc.div()

if __name__ == '__main__':

    a = int(input("请输入第一个数字: "))
    b = int(input("请输入第二个数字: "))

    calc = Calc(a, b)
    #test(calc)
    calc.add(a, b)
    calc.sub(a, b)
    calc.mul(a, b)
    calc.div(a, b)