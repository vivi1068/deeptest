# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 求和

def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum 

if __name__ == "__main__":
    print("元组传参，求和实例：")
    tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
    print(tuple_1)

    sum = sum_tuple(tuple_1)
    print("和为： %d" % sum)
    