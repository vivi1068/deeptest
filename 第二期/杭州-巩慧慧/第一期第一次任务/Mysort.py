#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-2 下午9:06
# @Author  : gonghuihui
# @File    : MySort
import random

class MySort:
    # 生成随机数,返回排序后的结果
    # start,end 限制随机数生成的范围
    # count 为生成随机数的个数
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.random_data = []

    # 生成随机数
    def __generator(self):
        for i in range(0, self.count):
            self.random_data.append(random.randint(self.start, self.end))

    # 排序
    def sort(self):

        self.__generator()
        # 计算长度
        l = len(self.random_data)

        # 冒泡排序
        for i in range(0, l):
            for j in range(1, l-i):
                if self.random_data[j-1] > self.random_data[j]:
                    self.random_data[j], self.random_data[j-1] = self.random_data[j-1], self.random_data[j]

        return self.random_data

if __name__ =="__main__":
    mysort_data = MySort(10, 1000, 100)

    data = mysort_data.sort()
    # 打印结果
    for d in data:
        print(d)





