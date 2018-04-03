#!/usr/bin/python
#coding:utf8

from __future__ import division

class Calc():
    # 初始化
    def __init__(self, a, b):
        self.a=a
        self.b=b

    # 加法
    def add(self):
        return self.a+self.b
    
    # 减法
    def sub(self):
        return self.a-self.b
    
    # 乘法
    def mul(self):
        return self.a*self.b

    # 除法
    def div(self):
        if self.b!=0:
            return round(self.a/self.b,2)
        return "error,divied by zero"

def test(calc):
    add=calc.add()
    sub=calc.sub()
    mul=calc.mul()
    div=calc.div()
    print(add,sub,mul,div)

if __name__ == "__main__":
    calc=Calc(5,6)
    test(calc)
    calc1=Calc(5,0)
    test(calc1)

