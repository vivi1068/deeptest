# __author__ ='wuwa'
# -*- coding: utf-8 -*-

class Deom():
    def __init__(self):
        print ('初始化')

    def out(self, text):
        print (text)

    def out_none(self):
        print('无需要传入参数')


class ChildDemo(Deom):
    def __init__(self):
        print ('我是子类的初始化')

    def out_none(self):
        print ('我重写了父类的out_noe方法')


if __name__ == "__main__":
    # 创建一个类对象
    new_obj = Deom()
    # 调用out方法
    new_obj.out('hello,python3')
    # 调用out_none
    new_obj.out_none()
    print ("=============我是分割线==========")
    # 创建子类的对对象
    child_obj = ChildDemo()
    # 调用父类的out方法
    child_obj.out("我调用的父类的out方法")
    # 调用子类自己的out_none方法
    child_obj.out_none()
