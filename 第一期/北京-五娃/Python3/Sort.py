# __author__ ='wuwa'
# -*- coding: utf-8 -*-
import random

'''
随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
'''
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.number_list = []

    # 实现排序，内部函数
    def __mysort(self):

        for i in range(0, self.count):
            elements = random.randint(self.start, self.end)
            self.number_list.append(elements)

        for i in range(0, self.count):
            for j in range(i + 1, self.count):
                if self.number_list[i] > self.number_list[j]:
                    self.number_list[i], self.number_list[j] = self.number_list[j], self.number_list[i]
        return self.number_list

    def prints(self):
        return self.__mysort()


# 使用示例
if __name__ == "__main__":
    # 打印排序后的结果
    sorted_data = MySort(10, 1000, 100)
    for num in sorted_data.prints():
        print(num)
