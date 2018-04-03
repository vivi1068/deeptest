#输入三个整数x,y,z，请把这三个数由小到大输出。

li = []
b = 0

while b < 3:
    a = int(input("请输入三个数字："))
    b += 1
    li.append(a)
li.sort()
print(li)
