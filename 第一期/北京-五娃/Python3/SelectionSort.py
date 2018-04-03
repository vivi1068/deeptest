# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
选择排序：每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完
1、从无序序列中选择一个“最小”元素，记录为R
2、与无序序列中的第一个元素比较后，一直找到无序中的最小的
3、将最小的数写进有序序列中
4、重复2、3
"""
import random


def generator():
    """
    随机生成一组无序序列
    :return:
    """
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))
    return random_data


def select_sort(data_list):
    """
    选择排序
    :return:
    """
    length = len(data_list)

    for i in range(0, length):
        min_ = i
        # 从剩余的无序序列中选择出最小的元素
        for j in range(i + 1, length):
            # 找到最小元素,将j所指向的值的索引指给min
            if data_list[min_] > data_list[j]:
                min_ = j
        # 在有序的后面追加，即交换比较的两个值的位置
        data_list[min_], data_list[i] = data_list[i], data_list[min_]
    return data_list


if __name__ == "__main__":
    # 生成无序序列
    random_data = generator()

    # 打印无序序列
    print(random_data)

    # 选择排序
    new_random_data = select_sort(random_data)

    # 打印排序结果
    print(new_random_data)
