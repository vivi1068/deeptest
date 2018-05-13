# -*- coding: UTF-8 -*-
# Filename ：Mysort.py 
# author by : 爱笑的眼睛
import random
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # �count为生成的随机数个数
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.lst = []

    # 实现排序，内部函数
    def __mysort(self):

        for i in range(0, self.count):
            elements = random.randint(self.start, self.end)
            self.lst.append(elements)
                                                   
        for i in range(0, self.count):
            for j in range(i + 1, self.count):
                if self.lst[i] > self.lst[j]:
                    self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        return self.lst

    def prints(self):
        return self.__mysort()


# 使用示例
if __name__ == "__main__":
    # 打印排序后的结果
    sorted_data = MySort(10, 100, 10)
    for num in sorted_data.prints():
        print(num)
