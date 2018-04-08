#!/usr/bin/python3
#coding=utf8

import random

class MySort():
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self,start,end,count):
        self.start=start
        self.end=end
        self.count=count
        self.data=[]
        for i in range(0,self.count):
            self.data.append(random.uniform(self.start,self.end))
        print(self.data)

    # 实现排序，内部函数
    def sort(self):
        n=len(self.data)
        data=self.data
        for i in range(0,n):
            for j in range(1,n-i):
                if data[j-1]<self.data[j]:
                    data[j-1],data[j]=data[j],data[j-1]
        return data

# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10,100,5)

    # 打印排序后的结果
    print(sorted_data.sort())
