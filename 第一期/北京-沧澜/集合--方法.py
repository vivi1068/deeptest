# -*- coding:utf-8 -*-

__author__ = 'zhangjin'

if __name__ == "__main__":
    print(u"set操作示例")

    set_source = set([1, 1, 2, 3, 4, 5, 6, 7])
    set_demo = set([1, 1, 2, 3, 4, 5, 6, 7])

    print(u"原始数据： ", end="")
    print(set_demo)

    # add方法，新增元素
    print(u"add后： ", end="")
    set_demo.add(9)
    set_demo.add(1)

    print(set_demo)

    # remove 删除元素
    print(u"remove后： ", end="")
    set_demo.remove(9)

    print(set_demo)

    # update 新增多个元素值
    list_demo = ["a", "b", "c"]
    set_demo.update(list_demo)

    print(u"update后： ", end="")
    print(set_demo)

