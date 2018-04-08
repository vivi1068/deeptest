# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/16:
-------------------------------------------------
"""
__author__ = 'Young'

#Dictionnary（字典）是Python最常用的数据类型，它使用方括号{}来标识，其元素为key-value对应，key与value用冒号:分割开

'''
Python中常用的内置函数有：

len
用于计算字典元素的个数, 即key的总数

str
输出字典，即以可打印的字符串输出字典

type
返回变量的类型
'''
if __name__ == "__main__":
    # 字典基本示例
    dict = {u"DeepTest": u"开源优测", u"book": u"快学Python3"}

    # 计算字典的长度
    print(len(dict))

    # 以字符方式输出字典,即将字典转换成字符串 并且判断类型
    str_d = str(dict)
    print(str_d,type(str_d))
    print(dict,type(dict))


    '''
    在python中，有大量的方法用于字典的处理,下面我们看看示例：
    
    clear
    清空字典
    copy
    复制字典
    fromkeys
    以序列作为kye创建一个新字典，value为所有键对应的初始值
    get
    返回指定key的value，如果key不存在，则返回默认值
    in
    判断key是否存在，是则返回True，否则返回False
    items
    返回可遍历的的元组，元组的元素为(key,value)形式
    keys
    返回字典的所有key
    setdefault
    如果key存在，则返回其对应的value，否则将该key和默认值插入到字典中，并返回默认值
    update
    更新字典
    values
    返回字典的所有value值
    '''
    print(u"--------------字典方法应用示例--------------")

    dict_demo = {u"DeepTest": u"开源优测", u"ebook": u"快学Python3"}
    tup1 = [1, 2, 3, 4]

    # copy复制字典
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    # fromkeys创建字典
    dict_new = dict.fromkeys(tup1, u"value")
    print(dict_new)

    # get获取指定key的value
    value1 = dict_demo.get(u"DeepTest", u"我是默认值")
    value2 = dict_demo.get(u"Python3", u"我是默认值")
    print(value1)
    print(value2)

    # in, 判断key是否存在
    key = u"DeepTest"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    # items, 以元组形式返回字典所有的(key, value)
    items = dict_demo.items()
    print("----->",items)

    # keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault(u"DeepTest", u"设置值")
    set_result2 = dict_demo.setdefault(u"我是key", u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # update, 更新字典
    dict_demo.update(dict_new)
    print(dict_demo)

    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)

    print(u"--------------字典遍历、修改、删除示例--------------")
    dict_demo = {u"DeepTest": u"开源优测", u"ebook": u"快学Python3"}

    # 遍历 方法1
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

        # 遍历 方法2
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

        # 修改
    dict_demo[u"ebook"] = u"修改后的值"
    print(dict_demo)

    # 删除指定元素
    del dict_demo[u"ebook"]
    print(dict_demo)

    # 清空字典
    dict_demo.clear()
    print(dict_demo)


#字典的value可以存储任何类型Python对象，即可以是标准的类型，也可以是我们自定义的类型，但key不可以。

#字典的key是唯一的，不可以重复

#字典的key可以是数字、字符串甚至元组，但不可以用列表
    print("key 列表示例")
    dict_demo = {u"['DeepTest1','DeepTest2']": u"开源优测", u"ebook": u"快学Python3"}



    for k in dict_demo:
        print(k,dict_demo[k])