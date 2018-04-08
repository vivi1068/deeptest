# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
函数语法
def 函数名（参数列表）:
   代码块
   return 返回值

   python中传递的对应可以分为“可更改对象”和“不可更改对象”
   可更改对象：列表、字典、结合
   不可更改对象：字符串、数值、元组
   参数定义的顺序：必选参数、默认参数、可变参数和关键字参数
"""


def sum(a, b):
    """
    计算两个数的和
    :param a:
    :param b:
    :return:
    """

    c = a + b
    return c


def sum_tuple(sumtuple):
    """
    元组传递
    :param sumtuple:
    :return:
    """
    sums = 0
    for i in sumtuple:
        sums += i
    return sums


def bar(arg1, arg2, key1=3, *args, **kwargs):
    """
    :param arg1: 普通参数
    :param arg2: 普通参数
    :param key1: 普通参数
    :param args: 非关键字可变参数，元组
    :param kwargs: 关键字参数，字典
    :return:
    """
    print("arg1 parameters is ", arg1)
    print("arg2 parameters is ", arg2)
    print("key1 parameter is ", key1)
    print("Arbitrary parameter is ", args)
    print("keywords parameter is ", kwargs)


if __name__ == '__main__':
    # 标准调用，数值5，6对应的参数为a，b，即a=5，b=6
    print('计算两个数的和', sum(5, 6))

    # 关键字调用
    print('计算两个数的和', sum(b=8, a=9))

    tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
    print('元组的和', sum_tuple(tuple_1))

    bar(11, 21, 3, 67, 78, k1=1, k2=2, k3=3)
