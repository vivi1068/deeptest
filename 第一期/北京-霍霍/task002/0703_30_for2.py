# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    print("九九乘法表：")
    for i in range(1, 10):
        for j in range(i, 10):
            print("%d * %d = %2d" % (i, j, i * j), end = " ")
        
        print("")

    print("计算0-100之间的偶数和")
    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2

    print("0-100间的偶数和= %d " % sum)

    print("九九乘法表实例：")
    n = 1

    while n <= 9:
        for m in range(n, 10):
            print("%d * %d = %2d" % (n, m, n*m), end = " ")
        print("")
        n = n + 1