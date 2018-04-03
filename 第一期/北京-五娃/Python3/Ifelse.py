# __author__ ='wuwa'
# -*- coding: utf-8 -*-
"""
语法结构：
if condition：
    代码块
else：
    代码块
    
注：condition 可以为单一条件也可以是复合条件，复合条件 通过 not、or、and 组合
if condition：
    代码块
elif condition：
    代码块
elif ....
else：
    代码块
    
注：当if为False时，会执行第一个elif，当第一个elif为Fales，执行下一个满足条件的elif 或者else代码块
    
if/elif/else语句嵌套


"""


def cmps(num):
    if num >= 10:
        print(u'num的数值大于或等于10')
    else:
        print(u'num的值小于10')


def cmp_new(num):
    if num > 0 and num < 10:
        print(u'num的值在0与10之间')

    elif num > 10 and num < 20:
        print(u'num的值在10与20之间')

    elif num > 20 and num < 30:
        print(u"num的值在20与300之间")

    else:
        print(u'num的值大约30')

def cmp_old(num):
    if num >0:
        if num<10:
            print(u'num的值在0与10之间')
        else:
            print(u'num的值大约10')
    else:
        print(u'num为负数')

        


if __name__ == "__main__":
    cmps(10)
    cmps(4)
    cmp_new(5)
    cmp_new(15)
    cmp_new(40)
    cmp_old(4)
    cmp_old(14)
    cmp_old(-4)

