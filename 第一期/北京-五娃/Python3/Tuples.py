# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
元组的元素不可修改
通过逗号分隔元素的方式创建元组，例如a,(a,),或者a, b, c or (a, b, c)
常用的内建函数 len、max、min、tuple
对元组进行合并、删除、运算、列表转元组
'''

if __name__ == "__main__":
    tuple_1 = (1, 2, 3, 4, 7, 67, 0)
    # 计算元组的长度
    print(len(tuple_1))

    # 返回元组中的最大值
    print(max(tuple_1))

    # 返回元组中的最小值
    print(min(tuple_1))

    # 将列表转换为元组
    list_1 = [1, 2, 3, 't', 'hello']
    print(list_1)
    list_to_tuple = tuple(list_1)
    print(list_to_tuple)

    # 对元组进行切片
    tuple_2 = ('hello', 'python', 3, 'yeah')

    # 因为元组也是序列，所以通过索引获取对应的值
    print(tuple_2[3])

    # 通过负索引获取对应的值
    print(tuple_2[-2])

    # 设置切片区间后，获取值,切片区间是闭开区间
    print(tuple_2[1:2])

    # 删除元组元素，元组元素无法被删除，只能删除整个元组,再次打印tuple_3时 会提示NameError异常
    tuple_3 = (2,)
    print(type(tuple_3))
    del tuple_3
    # print(tuple_3)

    # 合并元组,元组不可改变，只能对两个或者多个元组进行合并
    print(tuple_1 + tuple_2)

    # 元组复制
    print(tuple_2 * 2)

    # 字符串转为元组
    print(tuple('adnc'))

    # 遍历元组元素
    for i in tuple_1:
        print(i)
