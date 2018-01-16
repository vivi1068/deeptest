#_*_coding:utf-8_*_
if __name__ =="__main__":
    print("字典应用方法示例")
    dict_demo={"find":"百度","country":"中国","province":"河北"}
    tup1 = [1,2,3,4]
    #copy复制字典
    dict_copy = dict_demo.copy()
    print(dict_demo)
    print(dict_copy)
    print('-----------------------------------------------------')
    #fromkeys创建字典
    dict_new = dict_demo.fromkeys(tup1,"value")
    print(dict_new)
    print('------------------------------------------------------')
    #get获取指定key的默认值
    value1 = dict_demo.get("find","默认值")
    value2 = dict_demo.get("python3","默认值")
    print(value1)
    print(value2)
    print("------------------------------------------------------")
    #in ,判断key是否存在
    key = 'find'
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)
    print("-------------------------------------------------------")
    #items,已字典形式返回所有的value和key
    items = dict_demo.items()
    print(items)
    print("-------------------------------------------------------")
    #keys以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)
    print('--------------------------------------------------------')
    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault(u"DeepTest", u"设置值")
    set_result2 = dict_demo.setdefault(u"我是key", u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)
    #update ,字典更新
    dict_demo.update(dict_new)
    print(dict_demo)
    #values,返回字典中的所有values
    values = dict_demo.values()
    print(values)
