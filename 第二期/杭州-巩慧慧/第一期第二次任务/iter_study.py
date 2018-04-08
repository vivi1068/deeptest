#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 11:30
# @Author  : yulu
# @File    : iter_study
import sys

# 生成器函数
# 实现斐波纳契数列
def fibonacci(n):
    # 初始化变量
    a, b, count = 0, 1, 0

    while True:
        if count > n:
            return

        yield  a

        a, b = b, b + a
        count = count + 1

if __name__ == "__main__":

    seq_tuple = (1, 2, 3, 4, 5)

    # 创建迭代器
    seq_it = iter(seq_tuple)

    # 访问第一个元素
    print("第一个元素： %s" % next(seq_it))

    # 访问第二个元素
    print("第二个元素： %s" % next(seq_it))

    # 访问第三个元素
    print("第三个元素： %s" % next(seq_it))

    # 访问for循环来遍历迭代器对象
    print("\nfor循环迭代器对象： ")
    for_it = iter(seq_tuple)
    for i in for_it:
        print(i, end=" ")

    # 使用 while 结合next遍历迭代器对象

    print("\nwhile & next遍历迭代器对象： ")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()

    print("-----------------------------")

    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopAsyncIteration:
            sys.exit(0)

    #  为什么报错是正常的？？？