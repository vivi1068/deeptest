#!/usr/bin/python
#encoding=utf-8
__author__='小白龙'
def iffunc():
    number = input("请数据数字：")
    if str(number).isdigit():
        num = int(number)
        if num > 0 and num < 10:
            print(u"数值在0到10之间！")
        elif num >= 10 and num < 100:
            print(u"数值在10到100之间！")
        else:
            print(u"数值大于100！")
        return num
    else:
        print(u"输入错误，请输入正整数！")
        return 20


def forFuction(x):
    print(u"九九乘法表：")
    for i in range(1,10):
        for n in range(i,10):
            print('%d*%d=%d'%(i,n,i*n),end=" " )
        print()
    dic={"name":"小白龙","age":"18","other":"高富帅","really":"not"}

    print(u"for循环遍历字典：")
    for key in dic:
        print("%s:%s"%(key,dic[key]))

    print(u"while循环输出%d以内的质数"%x)
    i=3
    while i<x:
        for n in range(2,i):
            if i%n==0:
                i = i + 1
                break
            elif n==i-1:
                print(i)
                i=i+1



if __name__=='__main__':
    x=iffunc()
    forFuction(x)