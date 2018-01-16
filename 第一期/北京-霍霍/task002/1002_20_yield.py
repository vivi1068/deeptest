# -*- coding:utf-8 -*-
__author__ = "huohuo"

import sys

# 生成器函数
# 实现斐波那契数列
def fibonacci(n):
    # 初始化变量
    a, b, count = 0, 1, 0

    while True:
        if count > n:
            return

        yield a

        a, b = b, a + b
        count = count + 1

if __name__ == "__main__":
    # 初始化生成器函数，产生一个生成器函数
    f = fibonacci(10)

    while True:
        try:
            print(next(f), end=' ')
        except StopAsyncIteration:
            sys.exit(0)
