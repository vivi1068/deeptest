class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('Student object (name: %s) '% self.name)




# header = dict(zip(["fieldnames", "fieldnames"]))

print(zip(["fieldnames1", "fieldnames1"],["fieldnames2", "fieldnames2"]))
a=[1, 2,3]
b=[4, 5,6]

print(tuple(zip(a,b)))


## zip()函数单个参数
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
# 打印zip函数的返回类型
print("zip()函数的返回类型：\n", type(tuple1))
# 将zip对象转化为列表
print("zip对象转化为列表：\n", list(tuple1))