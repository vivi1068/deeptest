# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/16:
-------------------------------------------------
"""
__author__ = 'Young'


print("------------#random 实例----------")
list=["1","2","3","4"]
print(len(list))

'''
Python数值数据类型用于存储数值，并有一系列对应的函数用于处理数值类型的数据。

在Python中支持三种不同类型的数值类型：

整型(int)
通常称为整型或整数，为正数或负数，不带小数点。在Python3中，整型没有限制大小，即亦可做long类型使用，所以在Python3中无显性的long类型

浮点型(float)
即带小数点的数值，也可以用科学计数法表示:

1.2e2 = 1.2 * 10^2 = 1201.2e2=1.2∗10
2
 =120

复数(complex)
由实数部分和虚数部分构成，表达式方式为： a + bj 或 complex(a, b), 其中a为实数部分，b为虚数部分。
'''
print(range(10))
for i in range(10):
    print(i)
if __name__ == "__main__":
    print("------------转换---------------")
    x = 1.68
    y = 10

    # 将x转换为整数
    print(int(x))  # 将y转换为浮点数

    print(float(y))  # 将x转换为复数， 实数部分为x，虚数部分为0

    print(complex(x))

    print(complex(x, y))  # 将x，y转换为复数， 实数部分为x，虚数部分为y

    print("------------数值函数示例---------------")
    '''
    数学函数
    主要进行各种数学计算，例如计算绝对值、幂运算、平方根等等，主要定义在math模块中
    
    随机数函数
    主要用于随机数的处理，例如生成随机数主要定义在random模块中
    
    三角函数
    主要用于将数值转换为对应的三角弧度值，主要定义在cmath模块中
    
    数学常量
    Python中内置定义的数学常量，比如π
    '''
    import  math
    import  random
    import  cmath
    x = -100
    y = 1.9

    print(u"常用数学函数")
    # 返回x的绝对值
    print(abs(x))

    # 反回最大值
    print(max(x, y))

    # 返回最小值
    print(min(x, y))

    # 计算y^2
    print(pow(y, 2))

    # 返回平方根
    print(math.sqrt(y))

    print(u"常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # 从列表a中随机选中一个
    print(random.choice(a))

    # 从指定的范围(2-100按5递增的数据集)中随机选中一个
    print(random.randrange(2, 100, 5))

    # 生成一个随机数，它在(0,1)之间
    print(random.random())

    print(u"常用三角函数")
    x = 100

    # 返回x的反余弦弧度值
    print(cmath.acos(x))

    # 返回x的正弦弧度值
    print(cmath.sin(x))

    # 返回x的余弦弧度值
    print(cmath.cos(x))

    print(u"数学常量")
    print(cmath.pi)  # 返回π
