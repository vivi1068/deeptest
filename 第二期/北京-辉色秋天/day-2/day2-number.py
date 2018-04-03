# -*- coding:utf-8 -*-

import math
import cmath
import random

if __name__ == "__main__":
    y = 1.68
    x = -100
    
    print("常用函数")
   
    print("绝对值函数 abs(%d)=%d"%(x,abs(x)))

    print("最大值函数 max(%d, %d) is %d"%(x, y, max(x, y)))

    print("最小值函数 min(%d, %d) is %d"%(x, y, min(x ,y)))

    print("平方函数 pow(%d) = %d"%(x, pow(x,2)))

    print("平方根函数 sqrt(%d) is %d"%(y, math.sqrt(y)))

    a = [1, 3, 4, 5, 6, 8, 9, 10, 55, 96]

    print("a中随机数是 %d"%(random.choice(a)))

    print("100至200 间随机整数 是%d"%random.randint(100, 200))
    print("100至200间按5递增，选择随机数是%d"%random.randrange(100, 200, 5))

    print("随机输出0-1是%d"%random.random())
   
    z = 100
    print("反余弦弧度值",end='')
    print(cmath.acos(x))

    print("正余弦函数",end='')
    print(cmath.sin(x))

    print("余弦函数",end='')
    print(cmath.cos(x))

    print("π的值是%f"%cmath.pi)

