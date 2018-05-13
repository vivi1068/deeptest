# -*- coding:utf-8 -*-

#__author__ = u'smile eyes'

if __name__ == "__main__":
    print(u"list方法代码示例： ")
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9 , 0, 10 , 11]    
    
    # append，追加一个元素
    list1.append(100)
    print(list1)    
    
    # count, 统计1出现的次数
    count = list1.count(1)
    print(count)    
    
    # extend, 将list2追加到list1中
    list1.extend(list2)
    print(list1)    
    
    # index, 返回第一个2的索引
    index = list1.index(2)
    print(index)    

    # insert, 在列表第一个位置插入200
    list1.insert(0, 200)
    print(list1)    
    
    # pop, 删除最后一个元素
    list1.pop()
    print(list1)    
    
    # reverse, 把列表反向一下
    list1.reverse()
    print(list1)    
    
    # sort,对列表进行排序
    list1.sort()
    print(list1)    
    
    # copy，列表拷贝
    list3 = list1.copy()
    print(list1)
    print(list3)    

    # clear 清空列表
    list1.clear()
    print(list1)
    print(list3)