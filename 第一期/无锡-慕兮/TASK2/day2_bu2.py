# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

if __name__ == "__main__":
    print("list方法代码示例： ")
    list_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    list_2 = [11, 12, 13, 11, 12]

    # append，追加一个元素
    list_1.append(88)
    print(list_1)

    # count, 统计1出现的次数
    count = list_1.count(1)
    print("1出现的次数", count)

    # extend, 将list2追加到list1中
    list_3 = list_1.extend(list_2)
    print(list_1)
    print(list_3)

    # index, 返回第一个2的索引
    index = list_1.index(2)
    print(index)

    # insert, 在列表第一个位置插入200
    list_1.insert(0, 200)
    print(list_1)

    # pop, 删除最后一个元素
    list_1.pop()
    print(list_1)

    # reverse, 把列表反向一下
    list_1.reverse()
    print(list_1)

    # sort,对列表进行排序
    list_1.sort()
    print(list_1)

    # copy，列表拷贝
    list_4 = list_1.copy()
    print(list_4)

    # clear 清空列表
    list_4.clear()
    print(list_4)

    # 读取倒数第一个元素, 注意索引下标从0开始
    print(list_1[-1])

    # 读取第二个元素appium, 注意索引下标从0开始
    print(list_1[1])

    #切片，截取第2-4个元素
    print(list_1[1: 4])

    # 切片，截取从第2个元素开始后的所有元素
    print(list_1[1:])

    #更新元素
    list_1[0] = 999
    print(list_1)




