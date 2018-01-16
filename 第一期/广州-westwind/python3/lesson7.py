#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 22:47
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson7.py
# @Software: PyCharm
def if_demo():
    x = int(input("please input a number: "))
    if x >= 100:
        print("x is above 100")
    elif x >= 0:
        print("x is above 0")
    elif x < 0 :
        print("x is -")

if __name__ == "__main__":
    if_demo()