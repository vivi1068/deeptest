# -*- coding: UTF-8 -*-
# Filename ：Calc.py
# author by : 爱笑的眼睛
import re
class Calc:
    
    # 初始化
    def __init__(self, num1, num2):
        self.a = num1 
        self.b = num2
    
    # 加法
    def add(self):
        return self.a + self.b
        

    # 减法
    def sub(self):
         return self.a - self.b

    
    # 乘法
    def mul(self):
         return self.a * self.b

    # 除法
    def div(self):
        if self.b != 0:
            return self.a/self.b 
        else:
            return "只能输入数字"

             

if __name__ == '__main__':
    # 用户输入数字
    cal = Calc(4.8,2)
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())

    #用户输入的除数为0
    cal2=Calc(1,0)
    print(cal2.div())


   
         



