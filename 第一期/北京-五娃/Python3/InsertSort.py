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
    length = len(data_list)
    for i in range(1,length):
        key =data_list[i]
        j = i-1
        while j>=0:
            if data_list[j]>key:
                data_list[j+1] = data_list[j]
                data_list[j] = key
            j=j-1

    return data_list




if __name__ == "__main__":
    random_data = generator()
    print(random_data)
    random_data_1 =inset_sort(random_data)
    print(random_data_1)

