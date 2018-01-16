# -*- coding:utf-8 -*-\
__author__ = u'linan'

if __name__ == "__main__":
    tuple_demo = (1,2,3,4,5,6,7,8,9,0)

    #计算tuple_demo中元素的个数
    print(len(tuple_demo))

    #返回tuple_demo中最大值的元素
    print(max(tuple_demo))

    #返回tuple_demo中最小值的元素
    print(min(tuple_demo))

    #将list转换成元组
    list_demo = [1,2,3,4,5,6,7]
    tuple1 = tuple(list_demo)
    print(tuple1)


#切片
if __name__ == "__main__":
    print(u'元组切片')

    data_demo = (u"DeepTest",u"appium",u"testingunion.com",u"hellpo",u"python3")

    #读取第二个元素appium，注意索引下标从0开始
    e = data_demo[1]
    print(e)

    #读取倒数第二个元素hello
    e = data_demo[-2]
    print(e)

    #切片，截取从第2个元素开始后的所有元素
    e = data_demo[1:]
    print(e)

    #切片，截取第2个到第4个元素
    e = data_demo[1:4]
    print(e)

    #截取第3个到第5个元素
    e = data_demo[2:5]
    print(e)


#合并

if __name__ == "__main__":
    print(u"元组合并或连接操作示例")
    tup1 = (u"DeepTest",u"appium")
    tup2 = (u"testingunion.com",u"hrllo",u"python3")

    #合并成新的元组
    tup3 = tup1 + tup2
    print(tup1)
    print(tup2)
    print(tup3)

#运算

if __name__ == "__main__":
    print(u"元组运算示例")
    tup1 = (u"DeepTest",u"开源优测")
    tup2 = (1,2,3,4)

    #计算元组长度
    print(len(tup1))

    #元组连接
    tup3 = tup1 + tup2
    print(tup3)

    #元组复制
    tup4 = tup1 * 2

    #判断元素是否在元组中，是否赶回True,否则返回False
    result = 5 in tup2
    print(result)

    #遍历元组
    for t in tup2:
        print(t)


#删除
if __name__ == "__main__":
    print(u"元组合并或连接操作示例")
    tup1 = (u"DeepTest",u"appium")
    print(tup1)

    #删除元组
    del tup1
    print(tup1)