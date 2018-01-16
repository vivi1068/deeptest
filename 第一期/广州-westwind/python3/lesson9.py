#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 20:07
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson9.py
# @Software: PyCharm
def sum(a, b):
    #简单的求和
    c = a + b
    return c

def multi():
    "九九乘法表"
    data = []
    for i in range(1, 10):
        line = []
        for j in range(1, i + 1):
            line.append(u"%d * %d = %d " %(j, i , i * j))

        data.append(line)

    return data

def sum_tuple(seq):
    #元组传参
    sum = 0
    for s in seq:
        sum = sum + s
    return sum

def str_join(str1, str2, str3):
    #字符串传参
    return str1 + str2 + str3
if __name__ == "__main__":
    #调用函数，求和
    d = sum(1, 3)
    print(d)

    #九九乘法表
    data = multi()
    for d in data:
        print(d)

    print(u"元组传参求和实例：")
    tuple1 = (1, 33, 98, -1, 1000)
    print(tuple1)
    e = sum_tuple(tuple1)
    print(u"的和为：%d " %e)

    print(u"连接3个字符串")
    str1 = u"apple"
    str2 = u"中国"
    str3 = u"龙"
    f = str_join(str1, str2, str3)
    print("的结果是：%s" %f)