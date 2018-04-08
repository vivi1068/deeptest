#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 18:32
# @Author  : yulu
# @File    : func_study

def multi():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append(u"%d * %d = %2d" % (i, j, i*j))
        data.append(line)

    return data

def sum_tuple(seq):
    sum = 0
    for i in seq:
        sum = sum + i
    return sum

def str_join(str1, str2, str3):
    return str1 + str2 + str3

if __name__ == "__main__":
    # 无参传递
    print(u"九九乘法表： ")
    data = multi()
    for d in data:
        print(d)

    # 元组传递
    print(u"元组传参，求和事例：")
    tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
    print(tuple_1)

    sum = sum_tuple(tuple_1)
    print(u"和为： %d" % sum)

    # 字符串传递
    print(u"字符串连接实例： ")

    str1 = u"大家好,"
    str2 = u"我的公众号是："
    str3 = u"开源优测"

    str_j = str_join(str1, str2, str3)
    print(str_j)
