#!/usr/bin/python3

import sys

def fibonacci(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成

# 注释下面的循环试试看
while True:
    try:
        print (next(f), end=" ")
    except :
        # sys.exit()
        break

print(type(f))

l = [i for i in range(10)]
print(l)
m = (i for i in range(10))
print(m)

while True:
    try:
        print(next(m), end = " ")
    except :
        break

# let it go!
def fredm(n):
    a = 0
    for i in range(n):
        yield a
        a += 1
        print('pig')
    pass

dog = fredm(10)
while True:
    if next(dog) == 5:
        break
    pass

print('over')

# use iter open file
fl = open("test.txt","r")

def rdsize(file):
    re = 'aw21'
    for i in range(10):
        yield re
        re = file.read(1024)

reee = rdsize(fl)

print(next(reee))
print(next(reee))
print(next(reee))
