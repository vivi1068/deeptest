# __author__ ='wuwa'
# -*- coding: utf-8 -*-


def binary_search(seq, query):
    """
    :param seq: 待查序列
    :param query:要查找的目标
    :return:
    """
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2
        val = seq[mid]

        if val > query:
            end = mid - 1

        elif val < query:
            start = mid + 1

        else:
            # 返回对应的索引值
            return mid
    return None


def first_binary_search(seq, query):
    """
    first优先策略算法
    :param seq:
    :param query:
    :return:
    """
    start, end = 0, len(seq) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if (mid == 0 and seq[min] == query) or (seq[mid] == query and seq[mid - 1] < query):
            return mid
        elif seq[mid] < query:
            start = mid + 1
        else:
            end = mid - 1
    return None


def lsat_binary_seach(seq, query):
    start, end = 0, len(seq) - 1
    while start < end:
        mid = start + (end - start) // 2
        if (seq[mid] == query and mid == len(seq) - 1) or (seq[mid] == query and seq[mid + 1] > query):
            return mid
        elif seq[mid] < query:
            start = mid + 1
        else:
            end = mid - 1
    return None


if __name__ == "__main__":
    print("二分查找")
    seq = [2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
    print(seq)
    print("找到：", 5, " 索引是： ", binary_search(seq, 5))

    print("找到：", 4, " 索引是： ", binary_search(seq, 4))

    print("找到：", 13, " 索引是： ", binary_search(seq, 13))

    print("找到：", 2, " 索引是： ", binary_search(seq, 2))

    print("找到：", 25, " 索引是： ", binary_search(seq, 25))

    print ("first")
    print("找到：", 5, " 索引是： ", binary_search(seq, 5))

    print("找到：", 4, " 索引是： ", binary_search(seq, 4))

    print("找到：", 13, " 索引是： ", binary_search(seq, 13))

    print("找到：", 2, " 索引是： ", binary_search(seq, 2))

    print("找到：", 25, " 索引是： ", binary_search(seq, 25))

    print ("last")
    print("找到：", 5, " 索引是： ", binary_search(seq, 5))

    print("找到：", 4, " 索引是： ", binary_search(seq, 4))

    print("找到：", 13, " 索引是： ", binary_search(seq, 13))

    print("找到：", 2, " 索引是： ", binary_search(seq, 2))

    print("找到：", 25, " 索引是： ", binary_search(seq, 25))
