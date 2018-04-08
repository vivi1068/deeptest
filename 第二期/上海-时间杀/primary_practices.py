#!/usr/bin/python3

# 元组练习
tuple1 = ("a", "b", "c", "d", "e")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (u'deeptest', u'汉字', u'1')
tuple4 = ('deeptest', '汉字', '1')
tup5 = "ra", "cd", "tup", "fun"

# len、max、min函数
print(len(tup5))
print(max(tuple3))
print(min(tuple4))

# 链接、复制、迭代、判断存在
tup = tuple1 + tuple4
print(tup)
tup = tup * 2
print(tup)

del tup
tup = ()
for i in tuple2:
    tup += (i,)# 不加逗号试试

print(tup)

if 4 in tup:
    print('good')

# 元组索引、访问
print(tup[2])
print(tup[1:3])
print(tuple3[-2])

"""
#元组无法修改
tuple2[0] = (2,)# 2
"""

# 字典练习
# 增删改
dic1 = {'name':'deeptest', 'age':'10', 'class':'second'}

"""
# 键可以用数字、字符串、元组，不能用列表
dic2 = {'(li, la)':'xxx'}
dic3 = {'[ok]':'not'}
"""

print(dic1['name'])

dic1['age'] = 5
dic1['name'] = "deept"

print(dic1)

del dic1['name'] # 删除键 'Name'
print(dic1)

dic1.clear() # 清空字典
print(dic1)

del dic1

# len、str、type
dic2 = {'from':'qun', 'to':'dashi'}
# print(str(dic2))
print(type(dic2))

# copy fromkeys get items keys values
dic_new = dic2.copy()
dic_old = dict.fromkeys(tup)
dic_old1 = dict.fromkeys(tup, u"value") # value换成列表试试
print(dic_new, dic_old, dic_old1)

value = dic_old1.get(3)
print(value)

keys = dic_old1.keys()
values = dic_old1.values()
items = dic_old1.items() #((key,'value'),(key,'value')..)
print(keys,values) #前面自带dict_keys values items
print(items)

keys = type(keys)
print(keys) #非列表

# 遍历
for (key, value) in dic2.items():
    pass

for k, v in dic2.keys(), dic2.values():
    pass

# set 集合，特点是无序不重复
stu = {'amy', 'lili', 'andry', 'jack', 'jim', 'amy', 'tom'}
bok = (1, 2, 3, 4, 5, 6, 4)
print(stu, bok)

se = set('management')
print(se)

# add remove
stu.add('upo')
stu.remove('tom')
print(stu)

# - | & ^
a = set('bananarepatle')
b = set('appledates')

print(a - b)    # a和b的差集
print(a | b)    # a和b的并集
print(a & b)    # a和b的交集
print(a ^ b)    # a和b中不同时存在的元素
