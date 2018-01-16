# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

if __name__ == "__main__":
    tuple_1 = (1, 2, 3, 4, 5, 6)

    print("tuple的长度是：",len(tuple_1))
    print("tuple中的最大值是：", max(tuple_1))
    print("tuple的最小值是：", min(tuple_1))

    lista = [1, 3, 4, 5, 6, 8, 9]
    tuple_2 = tuple(lista)
    print("tuple2:", tuple_2)

    #合并tuple
    tuple_3 = tuple_1 + tuple_2
    print("tuple3:", tuple_3)

    #切片访问
    first = tuple_3[0]
    print("第一个值为：", first)

    end = tuple_3[-1]
    print("最后一个值为：", end)

    # 切片，截取从第2个元素开始后的所有元素
    slice_tuple = tuple_3[1:]
    print("从第2个元素开始后的所有元素", slice_tuple)

    # 切片，截取第2-4个元素
    slice_tuple2 = tuple_3[1: 4]
    print("从第2个元素到第四个元素", slice_tuple2)

    tuple_4 = tuple_1*4
    print(tuple_4)

    del (tuple_1)

    # 判断元素是否在元组中, 是则返回True, 否则返回
    result = 5 in tuple_4
    print(result)