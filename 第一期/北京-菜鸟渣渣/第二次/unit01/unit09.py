#coding=utf-8
class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #add
    def add(self):
        return self.a+self.b
    #sub
    def sub(self):
        return self.a-self.b
    #mul
    def mul(self):
        return self.a*self.b
    #div
    def div(self):
        if b!=0:

            return self.a/(self.b)
        raise "除数未0 ,非法"

a=int(input("请输入第一个数:"))
b=int(input("请输入第二个数:"))
calc=Calc(a,b)
print (calc.add())