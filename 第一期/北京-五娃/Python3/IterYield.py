# __author__ ='wuwa'
# -*- coding: utf-8 -*-
import sys


def create_iter(seq_tuple):
    # 创建迭代器 通过iter
    seq_iter = iter(seq_tuple)
    # 访问打印的元素 通过next访问元素
    print ("第一个元素：%s" % next(seq_iter))
    print ("第二个元素：%s" % next(seq_iter))
    print ("第三个元素：%s" % next(seq_iter))

    # for循环遍历迭代器对象
    for i in iter(seq_tuple):
        print ('for循环遍历迭代器：', i)

    # while 循环遍历迭代器
    while_it = iter(seq_tuple)
    while True:
        try:
            print ('while循环遍历迭代器', next(while_it))
        except StopIteration:
            sys.exit()


def fibonacci(n):
    '''
   生成器返回的是一个迭代器函数，只能用于迭代操作
   :return:
    '''
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    # seq_tuple = (1, 2, 3, 4, 5)
    # create_iter(seq_tuple)
    f = fibonacci(10)
    print(f)
    for i in f:
        print(i)
