# __author__ ='wuwa'
# -*- coding: utf-8 -*-
import random

"""
注意：将一个序列拆分为两部分来看，首个元素是是有序序列，除首个元素外的其他元素组成的是无序序列
1、从第一个元素开始，该元素可以认为已经被排序
2、取出下一个元素，在已经排序的元素序列中从后向前扫描（在有序序列里通过负索引和无序序列里的数进行比较，即从后向前扫描）
3、如果该元素（已排序）大于新元素，将该元素移到下一位置
4、重复步骤 3，直到找到已排序的元素小于或者等于新元素的位置
5、将新元素插入到该位置后
重复步骤 2~5
"""


def generator():
    """
    随机生成1-1000之间的无序序列
    :return:
    """
    rand_data = []
    for i in range(1, 10):
        rand_data.append(random.randint(1, 1000))
    return rand_data


def inset_sort(data_list):
    """
    插入排序，比较待插入的值与list中的值
    :return:
    """
    # 获取列表的长度
    length = len(data_list)

    # 在无序序列中选出一个元素
    for i in range(1, length):
        # 将待比较的元素值赋值给key
        key = data_list[i]
        # 假设第一个元素在一个有序序列中
        j = i - 1
        while j >= 0:
            # 比较有序序列的值与无序序列的值的大小
            if data_list[j] > key:
                data_list[j + 1] = data_list[j]
                data_list[j] = key
            j = j - 1

    return data_list


if __name__ == "__main__":
    # 生成无序序列
    random_data = generator()

    # 打印无序序列
    print(random_data)

    # 插入序列
    random_data_1 = inset_sort(random_data)

    # 打印排序结果
    print(random_data_1)
