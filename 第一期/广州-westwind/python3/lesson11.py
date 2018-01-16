#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 21:36
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson11.py
# @Software: PyCharm
import sys
def iterator():
    #迭代器
    seq_tuple = (1, 2, 3, 4, 5)

    #创建一个迭代器
    iterator_tuple = iter(seq_tuple)
    #访问打印第一个元素
    print(u"第一个元素为：%d" %next(iterator_tuple))

    print(u"第二个元素为： %d" %next(iterator_tuple))

    print(u"第三个元素为：%d" %next(iterator_tuple))

    #print(u"第四个元素为：%d" % next(iterator_tuple))

    print(u"\n\nfor循环遍历迭代对像")
    iterator_tuple = iter(seq_tuple)
    for t in iterator_tuple:
        print(t, end=" ")

    print(u"\n\nwhile, next遍历迭代")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()

def genarator():
    #生成器
    pass
def fibonacci(n):
    a, b , count = 0, 1, 0
    while True:
        if count > n:
            return n
        yield a
        a, b = b , a + b
        count = count + 1



if __name__ == "__main__":
    #iterator()
    f = fibonacci(10)
    while True:
        try:
            print(next(f))
        except StopAsyncIteration:
            sys.exit()