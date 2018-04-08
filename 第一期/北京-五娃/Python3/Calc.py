# __author__ ='wuwa'
# -*- coding: utf-8 -*-
'''
实现一个四则运算的类，要求实现任意两个数的加减乘除运算
'''


class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def __add(self):
        '''
        :return:self.a + self.b
        '''
        return self.a + self.b

    # 减法
    def __sub(self):

        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        # a / b 2和3版本的除法有稍许变化
        if self.b != 0:
            return self.a // self.b
        else:
            raise ('除数为0，无法计算！')

    # 加法
    def adds(self):
        return self.__add()

    # 减法
    def subs(self, ):
        return self.__sub()

    # 重置值
    def set(self, a, b):

        self.a = a
        self.b = b


if __name__ == "__main__":
    eg = Calc(2, 0)
    print(eg.adds())
    print(eg.subs())
    eg.set(9, 6)
    print(eg.mul())
    print(eg.div())
