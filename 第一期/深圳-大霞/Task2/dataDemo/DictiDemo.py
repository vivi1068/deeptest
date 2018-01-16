__author__ =u"大霞"
if __name__ =="__main__":
    dict ={u"DeepTest":"测试",u"book":u"快些python"}
    #计算字典的长度len
    print(len(dict))
    #以字符方式输出字典，即将字典转换成字符串
    str_d=str(dict)
    print(str_d)
    print(dict)
    #判断类型
    print(type(str_d))
    print(type(dict))

    dict_demo={u"DeepTest":u"开源优测",u"学习":u"快学Python",u"ebook":u"Python书籍"}
    tup=[1,2,3,4,5]
    #复制字典
    dict_cp=dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    #formkeys创建字典
    dict_new=dict.fromkeys(tup,u"values")#序列key和value至显示
    print(dict_new)
    #in 判断key是否存在
    key=u"DeepTest"
    result1=key in dict_demo
    result2=key in dict_new
    print(result1)
    print(result2)
    #items,以元组形式返回字典所有的（key,value）
    items=dict_demo.items();
    print(items)
    #keys 以列表形式返回字典所有的key
    keys=dict_demo.keys();
    print(keys)
    #setdefault,如果key存在，则返回其对应的value
    #否则将key和默认值插入到字典中，并返回默认值
    set_result1=dict_demo.setdefault(u"Deeptest","设置值")
    set_result2=dict_demo.setdefault(u"我是key",u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)
    #update 更新字典
    print(dict_new)
    dict_demo.update(dict_new)
    print(dict_demo)
    #values 返回字典中的所有value
    values=dict_demo.values()
    print(values)

    #字典的遍历、修改、删除
    dict_demo1 = {u"DeepTest": u"开源优测", u"学习": u"快学Python", u"ebook": u"Python书籍"}
    #遍历 方法1
    print(u"字典遍历 方法1：")
    for(key,value) in dict_demo1.items():
        print("%s:%s"% (key,value))
    #遍历 方法2
    print(u"字典遍历 方法2：")
    for key in dict_demo1.keys():
        print("%s:%s"% (key,dict_demo1[key]))
    #修改
    dict_demo1[u"ebook"]=u"修改后的值"
    print("打印修改后的字典值：")
    print(dict_demo1)
    #删除指定元素
    del dict_demo1[u"ebook"]
    print(dict_demo1)
    #清空字典
    dict_demo1.clear()
    print(dict_demo1)