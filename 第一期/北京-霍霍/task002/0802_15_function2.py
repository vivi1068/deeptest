# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 九九乘法表
def multi():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append("%d * %d = %2d " % (i, j, i*j))

        data.append(line)

    return data

if __name__ == "__main__":
    print("九九乘法实例：")
    data = multi() 
    for d in data:
        print(d) 