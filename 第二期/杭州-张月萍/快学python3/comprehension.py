# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import time

a = []
t0 = time.clock()
for i in range(1, 10000):
    a.append(i)
    #print(a)
print(time.clock() - t0, "seconds process time")

t1 = time.clock()
# 列表推导式
b = [i for i in range(1,10000)]
#print(b)
print(time.clock() - t1, "seconds process time")

# 求平方数
a1 = [i**2 for i in range(1,10)]
print(a1)

a2 = [i+1 for i in range(1,10)]
print(a2)

# 输出偶数
a3 = [i for i in range(1,10) if i % 2 ==0]
print(a3)

# 字符转小写
a4 = [letter.lower() for letter in 'ASDFGHJKLVBHKgdsfs']
print(a4)

# 字典推导式
a5 = {i:i+1 for i in range(1,4)}
print(a5)
a6 = {i:j for i,j in zip(range(4),'asdfg')}
print(a6)
a7 = {i.lower():j.upper() for i,j in zip('ASDFGXCVBsdf','dsgfdgSF')}
print(a7)

# 循环列表时获取元素索引，enumerate
letters = ['a', 'b', 'v', 'a', 'a', 'v', 'r', 'g']
for num,letter in enumerate(letters):
    print(letter, 'is', num+1)

# 词频统计
import string

#lyric = 'The night begin to shine, the night begin to shine'
path = 'D:/deeptest/第二期/杭州-张月萍/快学python3/Walden.txt'

with open(path, 'r') as text:
    # string.punctuation，去除符号,python对大小写敏感
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    print(words)
    # 将列表转化为集合
    words_index = set(words)
    # 创建单词为键，出现频率为值得字典
    counts_dict = {index:words.count(index) for index in words_index}

#for word in words:
    #print('{}-{} times'.format(word,words.count(word)))
# lambda 以字典中的值为排序的参数
for word in sorted(counts_dict, key=lambda x: counts_dict[x]):
    print('{}-{} times'.format(word,counts_dict[word]))




