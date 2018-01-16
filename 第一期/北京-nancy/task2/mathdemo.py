# -* coding:utf-8 *-
__author__ = 'nancy'

import math
import cmath
import random

if __name__ == "__main__":
    x = -100
    y = 1.9

    print(u"commmon math：")
    print(abs(x))
    print(max(x,y))
    print(min(x,y))
    print(pow(y,2))    #y^2
    print(math.sqrt(y)) #y's square root

    print(u"common random：")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(random.choice(a))
    print(random.randrange(2,100,5))  #(2,100) 按5递增
    print(random.random())  #(0,1)

    print(u"common cmath:")
    x = 100
    print(cmath.acos(x))
    print(cmath.sin(x))
    print(cmath.cos(x))

    print(u"constant:")
    print(cmath.pi)

'''
result is:
commmon math：
100
1.9
-100
3.61
1.378404875209022
common random：
4
77
0.5780858557339232
common cmath:
-5.298292365610485j
(-0.5063656411097588+0j)
(0.862318872287684+0j)
constant
3.141592653589793
'''
