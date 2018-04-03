# -*- coding:utf-8 -*-

__author__ = '米饭'


class Calc:
    # 初始化
    def __init__(self):
        print("初始化...")

    # 加法
    def add(self, a, b):
        return a + b

    # 减法
    def sub(self, a, b):
        return a - b

    # 乘法
    def mul(self, a, b):
        return a * b

    # 除法
    def div(self, a, b):
        if b != 0:
            return a / b
        elif b == 0:
            raise "被除数不能为0"

if __name__ == "__main__":
    # 主函数入口
    calc = Calc()
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    method = input("请输入运算方法，如+，-，*，/：")
    if method == "+":
        print(calc.add(num1, num2))
    elif method == "-":
        print(calc.sub(num1, num2))
    elif method == "*":
        print(calc.mul(num1, num2))
    elif method == "/":
        print(calc.div(num1, num2))
    else:
        print("请输入合法的运算符号！")