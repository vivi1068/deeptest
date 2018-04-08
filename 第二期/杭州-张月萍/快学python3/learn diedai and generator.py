# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import sys


seq_tuple = (1, 2, 3, 4, 5)

# 创建迭代器
seq_it = iter(seq_tuple)

# 访问打印第一个元素
print("第一个元素：%s" % next(seq_it))

# 访问打印第二个元素
print("第二个元素：%s" % next(seq_it))

# 访问打印第三个元素
print("第三个元素：%s" % next(seq_it))

# 使用for循环来遍历迭代器对象
print("\nfor循环来遍历迭代器对象:")
for_it = iter(seq_tuple)
for x in for_it:
    print(x, end='  ')

# 使用while结合next遍历迭代器对象
print("\n\nwhile & next 遍历迭代器对象：")
while_it = iter(seq_tuple)
while True:
    try:
        print(next(while_it))
    except StopIteration:
        sys.exit()


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
        #print(a, b)
        count += 1

if __name__ == "__main__":
    # 初始化生成器函数,产生一个生成器函数
    f = fibonacci(10)

    while True:
        try:
            print(next(f), end=' ')
        except StopIteration:
            sys.exit()
