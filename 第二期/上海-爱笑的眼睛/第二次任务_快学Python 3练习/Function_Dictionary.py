# -*- coding:utf-8 -*-

#__author__ = u'苦叶子'

if __name__ == "__main__":
    print(u"字典方法应用示例")

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
    print(items)    
    
    # keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)    
    
    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault(u"DeepTest", u"设置值")
    set_result2 = dict_demo.setdefault(u"我是key", u"我是value11")
    print(set_result1)
    print(set_result2)
    print(dict_demo)    
    
    # update, 更新字典
    dict_demo.update(dict_new)
    print(dict_demo)    
    
    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)

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