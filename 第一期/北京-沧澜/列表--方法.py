#_*_coding:utf-8_*_
if __name__ == "__main__":
    print("list方法代码示例")
    print("----------------------------")
    list1 = [1,1,2,1,2,3,4,5,6,7,8]
    list2 = [12,23,34,45,56,67,78,89]

    #append ,增加一个元素
    list2.append(100)
    print(list2)
    #count,统计1出现的次数
    counts = list1.count(1)
    print(counts)
    #extend ,将list2追加到list1之后
    list1.extend(list2)
    print(list1)

    #index,返回第一个2的索引
    index = list1.index(2)
    print(index)
    #insert，在列表第一个位置插入200
    list2.insert(0,200)
    print(list2)
    #pop,删除最后一个元素
    print('-------------------------')
    list1.pop()
    print(list1)
    #reverse ,把列表反向一下
    list1.reverse()
    print(list1)
    print(
        '-----------------------------------'
    )
    #sort,对列表进行排序
    list1.sort()
    print(list1)

    #copy,列表copy
    list3 = list1.copy()
    print(list1)
    print(list3)

    #清空列表
    list1.clear()
    print(list1)
    print(list3)