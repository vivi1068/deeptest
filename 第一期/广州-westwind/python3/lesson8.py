#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 0:00
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson8.py
# @Software: PyCharm
'''循环控制'''
def for_demo():
    tup1 = (1, 2, 3, 4, 5, 6, 7, 8)
    #遍历元组
    for x in tup1:
        print(x)

    #遍历list
    list1 = [u"python", u"java", u"c++"]
    for t in list1:
        print(t)

    #遍历dictionary
    dict1 = {"python": 3.5, "java": 1.8, "c++": 2015}
    for (key ,value) in dict1.items():
        print("%s : %s " %(key, value))

    for key in dict1:
        print((key,  dict1[key]))

    for x in range(1, 3):
        print(x)

    for x in range(1):
        print(x)

    for x in range(0, 10, 2):
        print(x)

    #九九乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d * %d = %d" %(i , j , i*j), end=" ")

        print(" ")

    x = 0
    sum = 0
    while x < 100:
        sum = x + sum
        x += 1
    print(sum)



if __name__ == "__main__":
    for_demo()