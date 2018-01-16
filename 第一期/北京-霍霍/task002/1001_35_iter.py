# -*- coding:utf-8 -*-
__author__ = "huohuo"

import sys

if __name__ == "__main__":
    seq_tuple = (1, 2, 3, 4, 5)

    # 创建迭代器
    seq_it = iter(seq_tuple)

    # 访问打印第一个元素
    print("第一个元素： %s " % next(seq_it))

    # 访问打印第二个元素
    print("第二个元素： %s " % next(seq_it))

    # 访问打印第三个元素
    print("第三个元素： %s " % next(seq_it))

    # for循环遍历迭代对象
    print("\nfor循环遍历迭代对象：")
    for_it = iter(seq_tuple)
    for x in for_it:
        print(x, end = ' ')

    # 使用while结合next遍历迭代器对象
    print("\nwhile结合next遍历迭代对象：")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()
