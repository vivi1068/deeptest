#!/usr/bin/python
#encoding=utf-8
__author__=u'小白龙'
class Calc:
    def add(self,a,b):
        if str(a).isdigit()&str(b).isdigit():
            return a+b
        else:
            print("数字不正确")
    def sub(self,a,b):
        if str(a).isdigit()&str(b).isdigit():
            return a-b
        else:
            print("数字不正确")
    def div(self,a,b):
        if str(a).isdigit()&str(b).isdigit():
            if b == 0:
                print("被除数不能为0")
                return
            else:
                return a / b
        else:
            print("数字不正确")
    def chen(self,a,b):
        if str(a).isdigit()&str(b).isdigit():
            return a*b
        else:
            print("数字不正确")

if __name__=="__main__":
    calc = Calc()
    print(calc.add(1,3))
    print(calc.chen(2,3))
    print(calc.sub(5,3))
    print (calc.div(4,0))