__author__ = "大霞"
if __name__ == "__main__":

    """
    python中常用的内置函数
    len用于计算元组元素的个数
    max返回元组元素的最大值
    min返回元组元素的最小值
    tuple将列表转换为元组
    """
    tuple1 = (u'deeptest', u'测试', u'练习')
    print(tuple1)
    tuple2 = (1, 3, 4, 5, 6)
    list_demo=[1,2,3,'a','b']
    #打印元组元素的个数
    print(len(tuple1))
    #打印元组元素的最大值
    print(max(tuple2))
    #打印元组的最小值
    print(min(tuple2))
    #将列表转换为元组
    print(tuple(list_demo))
    #切片
    print("切片：")
    data_demo=(u"DeepTest",u"appium",u"testingunion.com",u"hello",u"python3")
    #读取元组的第一个元素
    e=data_demo[0]
    print(e)
    #切片，截取元组从第二个开始后的所有元素
    e=data_demo[1:]
    print(e)
    #读取元组的倒数第一个元素
    e=data_demo[-1]
    print(e)
    tup=('a','test')
    print(tup)
    del tup
    #删除之后打印deu元组会报错
    #print(deu)
    tup1=(u'DeepTest','测试')
    tup2=(1,2,3,4,5)
    #运算符
    #计算元组长度
    print(len(tup1))
    #元组连接
    tup3=tup1+tup2
    print(tup3)
    #元组复制
    tup4=tup1*2
    print(tup4)
   # tup5=tup1*tup2
   # print(tup5)#can't multiply sequence by non-int of type 'tuple'
    #判断元素8是否存在元组tup2中，是则返回true，否则返回False
    result = 8 in tup2
    print(result)
    #遍历元组
    for i in tup2:
        print(i)
    #将元组转换为列表
    list1_demo=(1,2,3,4,5)
    print(list1_demo)
    list1=list(list1_demo)
    print(list1)
    