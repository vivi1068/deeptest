# -*- coding:utf-8 -*-
import math
import cmath
import random
__author__ = '高彩凤'

"""
    Number(数字)类型：int、float、complex
    常用数值函数：数学函数：绝对值、幂运算、平方根等。math模块。：运算的数学函数
                随机数函数：random模块
                三角函数：cmath模块：运算的是复数。
                数学常量：内置定义，pi，e等。
"""
if __name__ == "__main__":
    # 1.转换
    x = 1.68
    y = 10
    z = -1.2

    # 将x转换为整数
    print(int(x))
    # 将y转换为浮点数
    print(float(y))
    # 将x转换为复数，实数部分为x,虚数部分为0
    print(complex(x))
    # 将x, y转换为复数，实数部分为x，虚数部分为y
    print(complex(x, y))

    # 2.数值函数
    # 绝对值
    print(abs(z))
    # 幂运算
    print(pow(y, 3))
    # 最大值
    print(max(x, y, z))
    # 最小值
    print(min(x, y, z))
    # 平方根
    print(math.sqrt(y))
    # 随机数
    print(u"随机数")
    a = [1, 2, 3, 4, 5, 6]
    print(random.choice(a))
    # 从2,100按5递增中取随机数
    print(random.randrange(2, 100, 5))
    # 从0,1的随机数
    print(random.random())
    # 三角函数
    print(u"常用三角函数")
    x1 = 100
    print(cmath.acos(x1))
    print(cmath.sin(x1))
    print(cmath.cos(x1))
    print(u"数学常量")
    print(cmath.pi)
