#_*_coding:utf-8_*_
if __name__ == "__main__":
    print("字典的遍历、修改、删除示例")
    dict_demo = {"counry":"中国","province":"河北省","the city":"邯郸市","county":"大名县"}
    #遍历方法1
    for (key,value) in dict_demo.items():
        print("%s : %s" % (key,value))

    #遍历方法2
    print('----------------------------------')
    for key in dict_demo.keys():
        print("%s : %s" % (key,dict_demo[key]))

    #修改
    print('-----------------------------------')
    dict_demo["the city"]="city"
    print(dict_demo)
    #删除指定元素
    print('------------------------------------')
    del dict_demo["the city"]
    print(dict_demo)
    #清空字典
    print('------------------------')
    dict_demo.clear()
    print(dict_demo)
