#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

'''将一个列表的内容复制到另外一个列表中'''

print('请输入1/2/3选择使用复制的方式：1表示使用[:]，2表示使用for循环，3表示使用copy函数')

if(input()=='1') :

    '''使用[:]'''
    a=[1,2,3,4]
    b=a[:]
    print(b)

elif(input()=='2'):

    '''使用for循环'''
    a=[1,2,3,4]
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    print(b)

elif(input()=='3'):

    '''使用copy函数'''

    a = [1, 2, 3, 4]
    b = a.copy()
    print(b)