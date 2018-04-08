#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 12:40
# @Author  : yulu
# @File    : dict_study

if __name__ == "__main__":

    dict = {u"DeepTest": u"开源优测", u"book":u"快学python3"}
    tup1 = [1, 2, 3, 4]

    print(len(dict))

    str_d = str(dict)
    print(str_d)
    print(dict)

    print(type(dict))
    print(type(str_d))

    # copy复制字典
    dict_cp = dict.copy()
    print(dict)
    print(dict_cp)

    # fromkeys创建字典
    dict_new = dict.fromkeys(tup1, u"valus")
    print(dict_new)

    #get 获取指定的key的value
    value1 = dict.get(u"DeepTest", u"我是默认值")
    value2 = dict.get(u"Python3", u"我是默认值")
    print(value1)
    print(value2)

    # in 判断key是否存在
    key = u"DeepTest"
    result1 = key in dict
    result2 = key in dict_new
    print(result1)
    print(result2)

    # 以元组的形式返回字典所有的(key, values)
    items = dict.items()
    print(items)

    # keys 以列表的形式返回所有的key
    keys = dict.keys()
    print(keys)

    # setdefault, 如果key存在，则返回对应的value
    # 否则将key和默认值插入到字典中，并返回默认值
    set_result1 = dict.setdefault(u"DeepTest", u"设置值")
    set_result2 = dict.setdefault(u"我是key", u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict)

    # update 更新字典
    dict.update(dict)
    print(dict)

    # values 返回字典中所有的value
    values = dict.values()
    print(values)

    # 遍历 方法1
    for (key, value) in dict.items():
        print("%s : %s" % (key, value))

    # 遍历 方法2
    for key in dict.keys():
        print("%s : %s" % (key, dict[key]))

    # 修改
    dict[u"DeepTest"] = u"修改后的值"
    print(dict)

    # 删除指定元素
    del dict[u"book"]
    print(dict)

    # 清空字典
    dict.clear()
    print(dict)