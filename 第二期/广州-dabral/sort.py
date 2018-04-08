# !/usr/bin/python
# -*-coding:utf-8-*-

__author__ = 'dabral'

import random


class MySort(object):
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    # 实现排序，内部函数
    def __mysort__(self):
        # 初始化列表为空
        randiest = []

        for i in range(self.count):
            # 生成10到1000内的随机数
            num = random.randrange(self.start, self.end)

            if len(randiest) == 0:
                # 若是第一个数，直接插入列表
                randiest.insert(0, num)
            elif num <= randiest[0]:
                # 若比列表第一个数都小，在最前面插入随机数
                randiest.insert(0, num)
            else:
                # 随机数与已排好序的队列从前向后比较，查找到插入的位置进行插入
                j = len(randiest) - 1
                while num < randiest[j]:
                    j = j - 1
                randiest.insert(j + 1, num)

        # 返回排好序的随机数列表
        return randiest


# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10, 1000, 100)
    sortedList = sorted_data.__mysort__()

    print("列表长度是:", len(sortedList))
    # 打印排序后的结果
    print("排序后的列表是:", sortedList)


