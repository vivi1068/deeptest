# coding=utf-8


'''

快速排序（Quicksort）是对冒泡排序的一种改进。

快速排序由C. A. R. Hoare在1962年提出。

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。


'''

'''
基本过程

设要排序的数组是A[0]……A[N-1]，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。

值得注意的是，快速排序不是一种稳定的排序算法，也就是说，多个相同的值的相对位置也许会在算法结束时产生变动。

一趟快速排序的算法是：

设置两个变量i、j，排序开始的时候：i=0，j=N-1
以第一个数组元素作为关键数据，赋值给key，即key=A[0]
从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换
从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换
重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）

'''

import random


# 随机生成1-1000之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data


# 快速排序
def quick_sort(data_list, start, end):
    # 判断是否需要进行排序
    if start >= end:
        return data_list

        # 设置排序基准值，这里我们设置为第一个元素值
    base = data_list[start]
    left = start
    right = end
    while left < right:
        # 对data_list从右往左找第一个比base小的数的索引位置
        while left < right and data_list[right] >= base:
            right = right - 1

        # 对data_list从左往右找第一个比base大的数的索引位置
        while left < right and data_list[left] <= base:
            left = left + 1

        # 交换数据初步排序
        data_list[left], data_list[right] = data_list[right], data_list[left]

    # 把找到比base小的数据与base交换位置
    data_list[start], data_list[left] = data_list[left], data_list[start]



    # 进入下一轮排序
    quick_sort(data_list, start, left - 1)

    quick_sort(data_list, right + 1, end)
    return data_list


if __name__ == "__main__":
    print("开源优测-积微速成计划基本功")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    length = len(random_data)
    print(length)
    sorted_data = quick_sort(random_data, 0, length - 1)

    # 打印排序结果
    print(sorted_data)
