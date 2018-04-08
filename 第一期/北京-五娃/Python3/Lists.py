# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
列表是python中常用的一种数据类型，列表属于序列，可以通过索引访问其元素的值
通过[]表示一个列表
'''

if __name__ == "__main__":
    list_1 = [1, 2, 3, 8, 6, 8, 1, 0]

    # 列表的长度
    print(len(list_1))

    # 列表中的最大值
    print(max(list_1))

    # 列表中的最小值
    print(min(list_1))

    # 将元组转换为列表
    tuples = (1, 2, 3, 4)
    tuple_to_list = list(tuples)
    print(tuple_to_list)

    # 列表切片
    print(list_1[2:])
    print(list_1[2:4])
    print(list_1[:5])
    print(list_1[-3])

    # 向列表中添加元素,在列表的末端增加元素
    list_1.append(99)
    print(list_1)

    # 向列表中插入一个元素, 在索引值为4的位置插入元素120
    list_1.insert(4, 120)
    print(list_1)

    # 统计列表中某元素出现的个数
    print(list_1.count(8))

    # 两个列表合并,将列表list_1追加到列表list_2的尾部
    list_2 = [9, 45, 77, 56, 88]
    list_2.extend(list_1)
    print(list_2)

    # 返回匹配到的首个元素的索引值
    print(list_1.index(2))

    # 删除列表的最后一个元素，并返回其值
    pop = list_1.pop()
    print(pop)
    print(list_1)

    # 删除列表中匹配到的元素
    list_1.remove(0)
    print(list_1)

    print('将列表中元素反向排列后，重新输出')
    list_reverse =[123, 'xyz', 'zara', 'abc', 'xyz']
    print(list_reverse)
    list_reverse.reverse()
    print(list_reverse)

    # # 对列表进行排序
    list_3 = sorted(list_1)
    print(list_3)

    # 清空列表
    list_1.clear()
    print(list_1)

    # 复制列表
    list_2.copy()
    print(list_2)

    # 更新列表
    print(list_2)
    list_2[2] = 50
    print(list_2)
