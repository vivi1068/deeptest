#!/usr/bin/python
#encoding=utf-8

import random
__author__=u'小白龙'
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # �count为生成的随机数个数

    def getNum(self,start,end,count):
        numlist = []
        i = 0
        while i < count:
            i = i + 1
            numlist.append(random.randint(start,end))
        return numlist
    def numSort(self,list):

        for i in range(0,list.__len__()):
            for j in range(i+1,list.__len__()):
                if list[i]>list[j]:
                    temp =0
                    temp=list[i]
                    list[i]=list[j]
                    list[j]=temp
        return list


# 使用示例
if __name__ == "__main__":
    mysort = MySort()
    list = mysort.getNum(10,1000,100)
    print ("排序前：")
    print(list)
    print ("排序后：")
    print(mysort.numSort(list))

