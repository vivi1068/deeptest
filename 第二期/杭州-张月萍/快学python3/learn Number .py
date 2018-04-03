# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import math
import cmath   # 三角函数库
import random


if __name__ == "__main__":
    x = -100
    y = 2
    print("常用数学函数")
    # 返回x的绝对值
    print(abs(x))
    # 返回最大值
    print(max(x, y))
    # 计算y^3
    print(pow(y, 3))
    # 返回平方根
    print(math.sqrt(y))

    print("*" * 100)   # 分隔

    print("常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 从列表a中随机选中一个
    print(random.choice(a))
    # 从指定的范围（2-100按5递增的数据集）中随机选中一个
    print(random.randrange(2, 100, 5))
    # 生成一个随机数，在(0,1)之间
    print(random.random())

    print("*" * 100)   # 分隔

    print("常用三角函数")
    z = 100
    # 返回z的反余弦弧度值
    print(cmath.acos(z))
    # 返回z的正弦弧度值
    print(cmath.sin(z))
    # 返回z的余弦弧度值
    print(cmath.cos(z))

    print("*" * 100)   # 分隔

    print("数学常量")
    print(cmath.pi)

    x1 = 1.68
    y1 = 10

    # 将x转化为整数
    print(int(x1))
    # 将y转换成浮点数
    print(float(y1))
    # 将x转换为复数，实数部分为x，虚数部分为0
    print(complex(x1))
    # 将x，y转换为复数，实数部分为x，虚数部分为y
    print(complex(x1, y1))

