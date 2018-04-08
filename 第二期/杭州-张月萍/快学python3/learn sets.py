# -*- coding: utf-8 -*-
# __author__ = 'Carina'


if __name__ == "__main__":
    # 创建集合(无序、不重复)
    print("1、创建集合")
    set1 = set("chrome"  "chrome"  "firefox")
    set2 = set('1 1 2 3 1 1 4 4 5')
    print(set1)
    print(set2)
    print("*" * 50, "\n")

    # set操作示例
    print("2、set操作示例")

    set_source = set([1, 1, 1, 3, 2, 4, 2, 5])
    set_demo = set([1, 10, 1, 10, 3, 3, 6, 8])

    print("set_demo的原始数据：", end="")    # end=""表示不换行
    print(set_demo)
    print(type(set_demo))
    print("set_source的原始数据：", end="")
    print(set_source)
    print(type(set_demo))

    # 计算长度
    print(len(set_source))

    # add方法，添加重复元素，会被自动过滤掉
    print("add 9和1后：", end="")
    set_demo.add(9)
    set_demo.add(1)
    print(set_demo)

    # remove，删除元素
    print("remove 9 后：", end="")
    set_demo.remove(9)
    print(set_demo)
    # discard 删除元素
    print("discard 8 后：", end="")
    set_demo.discard(8)
    print(set_demo)

    # update,用于新增多个元素值，参数为list
    print("将set_source的值添加到set_demo：", end="")
    set_demo.update(set_source)   # 将set_source的值添加到set_demo
    print(set_demo)

    # issubset 判断s1中的每个元素是否都在s2中
    print("判断set_demo中的每个元素是否都在set_source中：", end="")
    set21 = set_demo.issubset(set_source)
    print(set21)

    # issuperset 判断s2中的每个元素是否都在s1中
    print("判断set_source中的每个元素是否都在set_demo中：", end="")
    set22 = set_demo.issuperset(set_source)
    print(set22)

    # union 并集，返回两个集合的并集
    print("set_demo和set_source的并集元素：", end="")
    set_demo1 = set([1, 2, 3, 1, 2, 3, 9])
    set_source1 = set([3, 3, 4 ,4 ,5, 8])
    set23 = set_demo.union(set_source)
    print(set23)

    #intersection交集，返回两个集合的交集
    print("set_demo和set_source的交集元素：", end="")
    set24 = set_demo.intersection(set_source)
    print(set24)

    #difference 返回s1中有s2中没的元素
    print("set_demo中有，set_source中没有：", end="")
    set25 = set_demo.difference(set_source)
    print(set25)

    # symmetric_difference  对称差集 取s1中有s2中没有的，s2中有s1中没有的
    print("set_demo和set_source的对称差集：", end="")
    set26 = set_demo.symmetric_difference(set_source)
    print(set26)

    # clear
    print("set_demo清空后：", end="")
    set27 = set_demo.clear()
    print(set27)

    #集合不能切片
    #print(set_demo(1,2))
