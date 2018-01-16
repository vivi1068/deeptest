# -*- coding:utf-8 -*-

__author__ = u'linan'

if __name__ == "__main__":
    list_demo = [1,2,3,4,5,6,7,8,9,0]

    print(u"内置函数处理list示例")

    #计算list_demo中的元素个数
    print(len(list_demo))

    #计算list_demo中最大值的元素
    print(max(list_demo))
    
    #计算list_demo中最小值元素
    print(min(list_demo))

    #将list转换成元组
    list_demo = (1,2,3,4,5,6)
    list1 = list(list_demo)
    print(list1)


#list方法
if __name__ == "__main__":
    print(u"list方法示例")
    list1 = [1,1,2,2,3,3,3,4,5,6]
    list2 = [7,8,9,0,10,11]

    #append.追加一个元素
    list1.append(100)
    print(list1)

    #count统计1出现的个数
    count = list1.count(1)
    print(count)

    #extend,将list2追加到list1中
    list1.extend(list2)
    print(list1)

    #index，返回第一个2的索引
    index = list1.index(2)
    print(index)

    #insert,在列表第一个位置插入索引
    list1.insert(0,200)
    print(list1)

    #pop，删除列表最后一个元素
    list1.pop()
    print(list1)

    #reverse,将列表反向一下
    list1.reverse()
    print(list1)

    #clear清空列表
    list1.clear()
    print(list1)
    print(list2)

#切片
if __name__ == "__main__":
    print(u"列表切片示例")

    data_demo = [u"DeeoTest",u"appium",u"testingunion.com",u"hello",u"python3"]

    #读取第二个元素appium
    e = data_demo[1]
    print(e)

    #读取倒数第二个元素hello
    e = data_demo[-2]
    print(e)

    #切片截取第2到第4个元素
    e = data_demo[1:4]
    print(e)

#列表更新

if __name__ == "__main__":
    print(u"列表更新操作示例")

    data_demo =  [u"DeeoTest",u"appium",u"testingunion.com",u"hello",u"python3"]
    print(data_demo)

    #把hello改为hello world
    data_demo[3] = u"hello world"
    print(data_demo)