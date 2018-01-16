__author__ = u"大霞"
#集合练习set
if __name__ == "__main__":
    #集合为无序的、不重复的
    set1=set(u"Deeptest Deeptest")
    print(set1)
    print(u"set操作示例")
    set_source=set([1,1,2,3,4,5,6,7])
    set_demo=set([1,1,2,3,4,5,6,7])
    print(u"原始数据：",end="")
    print(set_demo)
    #add方法，新增元素
    print(u"add后：",end=" ")
    set_demo.add(9)
    set_demo.add(1)
    print(set_demo)
    #remove删除元素
    print(u"remove后：", end=" ")
    set_demo.remove(9)
    print(set_demo)
    #update新增多个元素值
    list_demo=["a","b","c"]
    set_demo.update(list_demo)
    print(u"update后：", end=" ")
    print(set_demo)
