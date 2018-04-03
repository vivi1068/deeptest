# -*- coding: utf-8 -*-
# __author__ = 'Carina'


# 计算圆的面积
import math

banjing = int(input("Enter banjing:"))
a = 2
area = math.pi * banjing ** a
print("半径为{} 的圆的面积是{:.10f}".format(banjing,area))
