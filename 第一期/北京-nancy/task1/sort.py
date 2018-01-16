#!/usr/bin/python
# coding=utf-8
# Filename: sort.py
# 2018-01-10
__author__ = "nancy"

import random

# 随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数

class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.random_list = []

    # generate random num
    def __generatenum__(self):
        for i in range(0,self.count):
            self.random_list.append(random.randint(self.start, self.end))
        print('random num is：%s'%(self.random_list))

    # 实现排序，内部函数
    def __mysort__(self):
        self.__generatenum__()

        #sort
        for i in range(0,len(self.random_list)):
            tmp = self.random_list[i]
            j = i
            while (j > 0 and self.random_list[j-1] > tmp):
                self.random_list[j] = self.random_list[j-1]
                j = j-1
            self.random_list[j] =tmp

        return self.random_list
# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10,1000,100)

    # 打印排序后的结果
    print(sorted_data.__mysort__())


