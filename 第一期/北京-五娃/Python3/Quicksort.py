# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
快速排序
1、设置两个变量i、j，排序开始的时候：i=0，j=N-1；
2、以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
3、从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
4、从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
5、重复第3、4步，直到i=j；
注意：在3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。
     找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。
"""
import random


def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data


def quick_sort(data_list, start, end):
    """
    快速排序
    :return:
    """
    if start >= end:
        return data_list

    # 选择一个元素作为排序序列基准值
    base = data_list[start]
    left = start
    right = end

    while left < right:
        # 从右往左查找比base小的元素，将查找到的元素移到左侧
        while left < right and data_list[right] >= base:
            right = right - 1
            data_list[left] = data_list[right]
        # 从左往右找比base大的元素，将找到的元素移动到右侧
        while left < right and data_list[left] <= base:
            left = left + 1
            # 交换找到元素的位置
            data_list[right] = data_list[left]

    # left 与right相等时即结束了比较，需要将这个数设置回base
    data_list[right] = base

    # 进入下一轮排序
    quick_sort(data_list, start, left - 1)

    quick_sort(data_list, right + 1, end)

    return data_list


if __name__ == "__main__":
    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    length = len(random_data)
    sorted_data = quick_sort(random_data, 0, length - 1)

    # 打印排序结果
    print(sorted_data)
