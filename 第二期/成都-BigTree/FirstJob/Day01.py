# -*- coding:utf-8 -*-

__author__ = "BigTree"


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 重置数据
    def set(self, a, b):
        self.a = a
        self.b = b

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
            # 保留小数点后4位
            return round(self.a / self.b, 4)
        else:
            print("除数为0，非法")