
'''
概述

在上文《二分查找》中，我们了解了二分查找基本实现原理和具体的实现算法。

但大家有没有发现，如果目标查找值，如果在查找序列中存在多个，则查找返回的索引值，会有所变化。

那下面我们试着利用二分查找实现以下功能：

查找目标值在序列中第一次出现时的索引

查找目标值在序列中最后一次出现时的索引

例如，有序列如下：

seq = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
我们查找目标值： 5

第一次出现在索引为：4 的位置
最后一次出现在索引为：7 的位置
下面我们对二分查找算法进行策略改造升级为：

# 用于实现二分查找第一次出现的算法
first_binary_search(seq, query)

# 用于实现二分查找最后一次出现的算法
last__binary_search(seq, query)


'''
# rst二分查找算法
# seq   待查序列
# query 要查找的目标

# first二分查找算法
# seq   待查序列
# query 要查找的目标
def first_binary_search(seq, query):
    # start为起始索引
    # end  为结束索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2  # // 整除
        if (mid == 0 and seq[mid] == query) or(seq[mid] == query and seq[mid - 1] < query):
            # 这是实现first的最关键判断
            # 在seq中找到目标query第一次出现的位置
            # 返回对应的索引值
            return mid
        elif seq[mid] < query:
            # 目标值大于中间值
            # 说明目标值在mid - end之间
            start = mid + 1
    else:
        # 目标值小于于中间值
        # 说明目标值在start - mid之间
        end = mid - 1


# 目标值不存在于seq中，返回None
    return None

if __name__ == "__main__":
    print("二分查找first示例")
    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    # 返回7
    print("5第一次出现的索引位置为： ", first_binary_search(seq, 5))

    # 返回13
    print("7第一次出现的索引位置为： ", first_binary_search(seq, 7))

    # 返回15
    print("8第一次出现的索引位置为： ", first_binary_search(seq, 8))
    #last优先策略算法实现

# -*- coding:utf-8 -*-





# last二分查找算法
# seq   待查序列
# query 要查找的目标
def last_binary_search(seq, query):
    # start为起始索引    # end  为结束索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2  # // 整除
        if (seq[mid] == query and mid == len(seq) - 1) or(seq[mid] == query and seq[mid + 1] > query):
            # 这是实现last的最关键判断
            # 在seq中找到目标query第一次出现的位置
            # 返回对应的索引值
            return mid
        elif seq[mid] < query:
            # 目标值大于中间值
            # 说明目标值在mid - end之间
            start = mid + 1
        else:
            # 目标值小于于中间值
            # 说明目标值在start - mid之间
            end = mid - 1

    # 目标值不存在于seq中，返回None
    return None


if __name__ == "__main__":
    print("二分查找last示例")
    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    # 返回9
    print("5最后一次出现的索引位置为： ", last_binary_search(seq, 5))

    # 返回14
    print("7最后一次出现的索引位置为： ", last_binary_search(seq, 7))

    # 返回15
    print("8最后一次出现的索引位置为： ", last_binary_search(seq, 8))
