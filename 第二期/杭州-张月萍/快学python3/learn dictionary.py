# -*- coding: utf-8 -*-
# __author__ = 'Carina'


if __name__ == "__main__":
    # 创建示例
    print("1、创建示例")
    dict11 = {"key1": "value1", "key2": "value2"}
    dict12 = {12: "appium", "zidonghua": "Python"}
    print(dict11)
    print(dict12)
    print("*" * 50, "\n")

    # 内置函数
    print("2、内置函数功能演示")
    dict21 = {"wenhouyu": "hello", "zaijian": "see you"}
    print("字典dict21：", dict21)
    # 计算长度
    print("字典dict21的长度为：", len(dict21))
    # 字典转换为字符串
    print("以字符形式输出dict21：", str(dict21))
    print("以集合形式输出dict21：", set(dict21))
    print("以列表形式输出dict21：", list(dict21))
    print("以元组形式输出dict21：", tuple(dict21))
    # 判断类型
    print(type(str(dict21)))
    print(type(dict21))
    print(type(set(dict21)))
    print(type(list(dict21)))
    print("*" * 50, "\n")

    # 方法
    print("3、字典的方法功能演示")
    dict_demo = {"yingyu": "English", "zhongwen": "Chinese"}
    tuple1 = [1, 2, 3, 4]
    print("dict_demon内容为：", dict_demo)
    print("tuple1内容为：",tuple1)

    # 复制
    dict_cp = dict_demo.copy()
    print("复制dict_demo：", dict_cp)

    # 以序列作为key创建一个新字典，value为所有键对应的初始值
    dict_new = dict.fromkeys(tuple1, "happy")
    print("已tuple1创建字典：", dict_new)

    # 获取指定key的value值
    value1 = dict_demo.get("yingyu", "我是默认值")
    value2 = dict_demo.get("zhongwen", "我是默认值")
    print(value1)
    print(value2)

    # in ,判断key是否存在
    key = "zhongwen"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    # items，以元组形式返回字典所有的key和value
    items = dict_demo.items()
    print(items)

    # keys,以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault, 如果key存在，则返回其对应的value，否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault("yingyu", "nihao")
    set_result2 = dict_demo.setdefault("riyu", "Japan")
    print(set_result1)
    print(set_result2)

    # values,返回字典中所有的value
    values = dict_demo.values()
    print("字典中所有的value：", values)
    print("*" * 50, "\n")

    # 遍历、新增、修改、删除
    print("4、字典遍历、修改、删除演示")
    # 遍历方法1
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

    # 遍历方法2
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

    # 新增
    # 往字典中添加单一元素
    dict_demo["yingwenming"] = "carina"
    # update 更新字典
    dict_demo.update(dict_new)   # 往字典中添加多个元素
    #dict_demo1 = dict_demo.update["yingyu": "YY"]  #更新某个值
    print("dict_new更新到dict_demo，数据合并：", dict_demo)


    # 修改
    dict_demo["zhongwen"] = "中文"
    print(dict_demo)

    # 删除指定元素
    del dict_demo["yingyu"]
    print("删除yingyu后：", dict_demo)

    # 清空字典
    dict_demo.clear()
    print("清空字典后：", dict_demo)

    #键值不重复,若重复则取最后一个值
    dict_cf ={'key':'123','key':'12','key':'hi'}
    print(dict_cf)

    print("*" * 50)

    # 字典不能切片
    #print(dict_demo[1:2])
    # 缺少值，字典中键与值不能脱离对方而存在
    #dict_demo1 = {'BAIDU':}
    #print(dict_demo1)
    # 将一个可变的元素作为key，比如列表􀁏􀁈􀒂􁌱􀘲􁔰􀖢􀔅􀀃􀁎􀁈􀁜􀀃􀹶􀺅􀭌􀨁􀙎?􀓞􀓻􀝢􀝒􀒁􀁐􀁘􀁗􀁄􀁅􀁏􀁈􀒂􁌱􀘲􁔰􀖢􀔅􀀃􀁎􀁈􀁜􀀃􀹶􀺅􀭌􀨁􀙎􀩙􀓞􀓻􀝢􀝒􀒁􀁐􀁘􀁗􀁄􀁅􀁏􀁈􀒂􁌱􀘲􁔰􀖢􀔅􀀃􀁎􀁈􀁜􀀃􀹶􀺅􀭌􀨁􀙎
    dict_test = {[]: 'a test'}    #报错：unhashable type: 'list'
    print(dict_test)




