#!/usr/bin/python3

import random


# 循环逻辑练习
lists = []
for i in range(100):
    lists.append(random.randint(10, 100))

# for + while循环（神奇的一幕，只循环10次）
n = 0
for i in range(11):
    while i != n:
        lists[i - 1], lists[i] = lists[i], lists[i - 1]
        n += 1
        print(i)

print('game over')

# continue、break练习
# 变量为 3 时跳过输出
var = 6
while var > 0:
    var -= 1
    if var == 3:
        continue
    print('var值 :', var)


# 正宗的乘法口诀表
for i in range(10):
    k = i
    for j in range(10):
        if j == k:
            print(i, '*', j, '=', i * j)
            break
        print(i, '*', j, '=', i * j, end=' ')

# for else（如果循环中有过break则执行else语句，否则不执行）
for n in range(2, 10):
    for x in range(2, 10):
        if (n % x) == 0:
            if n ==x:
                continue
            else:
                print(n, ' is not 质数')
                break
    else:
        print(n, ' is 质数')

# while + else（如果循环中有过break则不执行else语句，否则执行）
count = 0
while count < 5:
    print(count, ' 小于 5')
    count += 1
    # break
else:
    print(count, ' 大于或等于 5')



