# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

'''
if __name__ == "__main__":
    x = 1.68
    y = 10

    # 将x转换为整数
    print(int(x))
    # 将y转换为浮点数
    print(float(y))
    # 将x转换为复数， 实数部分为x，虚数部分为0
    print(complex(x))
    # 将x，y转换为复数， 实数部分为x，虚数部分为y
    print(complex(x, y))

import math
import cmath
import random

if __name__ == "__main__":
    x = -100
    y = 1.9

    print("常用数学函数")
    # 计算绝对值
    print(abs(x))
    
    # 计算最大值
    print(max(x, y))
    
    # 计算最小值
    print(min(x, y))
    
    # 计算y^2
    print(pow(y, 2))
    
    # 返回平方根
    print(math.sqrt(y))
    
    # 返回log10 log2
    print(math.log10(y))
    print(math.log2(y))

    print("常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    #打印a中的某一个值
    print(random.choice(a))
    
    #打印2至100中以5为间隔的其中一个值
    print(random.randrange(2, 100, 5))
    
    #打印0-1之间的数
    print(random.random())

    print("常用三角函数")

    x = 100

    #返回x的反余弦弧度值
    print(cmath.acos(x))
    
    #返回x的正弦弧度值
    print(cmath.sin(x))
    
    #返回x的余弦弧度值
    print(cmath.cos(x))

    print("数学常量pi")
    print("数学常量pi", cmath.pi)
''''''
if __name__ == "__main__":

    t = ('1', '2', '3', '4', '5', '6', '7', '8')
    # 用 - 将t中元素合并成一个新的字符串
    str_t = "-".join(t)
    print(str_t)

    # 将str_t以-进行切割
    str_s = str_t.split("-")
    print(str_s)

    # 将t中元素合并成一个新的字符串
    str_n = "".join(t)
    print(str_n)
    print("字符串常用方法")
    source_str = "  你好，hello, my name is Lakisha, I am from Jiangxi provence, hello hello hello, thanks thanks  "

    #从左往右找
    print(source_str.find("hello"))
    print(source_str.index("hello"))

    # 从右往左查找yo
    print(source_str.rfind("hello"))
    print(source_str.rindex("hello"))

    # 替换所有的 hello
    print(source_str.replace("hello", "nihao"))

    #替换两个hello
    print(source_str.replace("hello", "ni hao", 2))

    print("去字符串前后空格")
    print(source_str.lstrip())
    print(source_str.rstrip())
    print(source_str.strip())
'''
if __name__ == "__main__":
    str_1 = "123456789"
    str_2 = "abcdEFGHI"
    str_3 = "12345abcdefGHIJKL"
    str_4 = "abcde"
    str_5 = "ABCDE123"
    str_6 = "        "
    str_7 = " asbcdf"

    #isalnum
    print("是不是都是字母数字的组合", str_1.isalnum())
    print(str_3.isalnum())

    #isallow
    print("是不是都是字母的组合", str_2.isalpha())

    #islower
    print("是不是字母都是小写字母的组合", str_2.islower())

    #isupper
    print("是不是字母都是大写字母的组合", str_5.isupper())
    print("是不是字母都是大写字母的组合", str_3.isupper())

    #isdigit
    print("是不是都是数字的组合",str_2.isdigit())
    print(str_3.isdigit())
    print(str_1.isdigit())

    #isspace
    print("是不是都是空格的组合",str_7.isspace())
    print(str_6.isspace())

