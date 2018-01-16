# -*- coding:utf-8 -*-
__author__ = "huohuo"

class DemoClass:
    def __init__(self):
        print("初始化")

    def output(self, text):
        # 输出text到console
        print(text)

    def output_none(self):
        # 不带参数的方法
        print("我不能传入参数")

# 继承DemoClass
class ChildDemoClass(DemoClass):
    def __init__(self):
        print("我是子类")

    # 重写output_none
    def output_none(self):
        print("我是子类不能传参的方法")

if __name__ == "__main__":
    # 创建一个类对象
    demo_obj = DemoClass()

    # 调用output
    demo_obj.output("我是参数")

    # 调用output_none
    demo_obj.output_none()

    print("-------------------")

    # 创建子类的对象
    child_demo_obj = ChildDemoClass()

    # 调用output,调用的是父亲的方法
    child_demo_obj.output("我是参数")

    # 调用output_none,调用的是重写后的方法
    child_demo_obj.output_none()

