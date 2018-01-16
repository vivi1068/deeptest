# -*- coding:utf-8 -*-
__author__ = "Lakisha"
'''
if __name__ == "__main__":
    #字典基本示例
    dict = { "DeepTest": "开源优测", "book": "快学python3"}

    #计算字典的长度
    print(len(dict))

    #义字符方式输出字典，即将字典转成字符串
    str_d = str(dict)
    print(str_d)
    print(dict)

    #判断类型
    print(type(str_d))
    print(type(dict))

    tup1= [1, 2, 3, 4]

    #copy复制字典
    dict_cp = dict.copy()
    print(dict_cp)
    print(dict)

    #fromkeys 创建字典
    dict_now = dict.fromkeys(tup1, "value")
    print(dict_now)

    #get 获取指定key的value
    value1 = dict.get("DeepTest", "woshimorenzhi")
    value2 = dict.get("python3","book")
    print(value1)
    print(value2)

    #in, 判断key 是否存在
    key = "DeepTest"
    result1 = key in dict
    result2 = key in dict_now
    print(result1)
    print(result2)

    # items, 以元祖返回字典所有的（key， value）
    items = dict.items()
    print(items)

    #keys, 以列表形式返回字典所有的key
    keys = dict.keys()
    print(keys)

    #setdefault, 如果key存在，则返回其对应的value
    #否则将该key和默认值插入到字典中，并返回默认值
    set_default1 = dict.setdefault("DeepTest","morenzhi")
    set_default2 = dict.setdefault("python3", "morenzhi")
    print(set_default1)
    print(set_default2)
    print(dict)

    #update，更新合并字典
    dict.update(dict_now)
    print(dict)

    #values 返回字典中所有的value
    values = dict.values()
    print(values)
'''
if __name__ == "__main__":
    dict = {"DeetTest":"开源优测", "book":"快学Python3"}

    #遍历方法1
    for (key, value) in dict.items():
        print("%s : %s"%(key, value))

    # 遍历方法2
    for key in dict.keys():
        print("%s : %s"%(key, dict.get(key)))

    for key in dict.keys():
        print("%s : %s"%(key, dict[key]))

    #修改
    dict["ebook"] = "xiugaikuaixue"
    print(dict)

    #删除指定元素
    del dict["ebook"]
    print(dict)

    #清空字典
    # dict.clear()
    print(dict)
