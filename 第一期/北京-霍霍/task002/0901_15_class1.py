# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 定义一个基本类
class DemoClass:

    def __init__(self):
        print("初始化")

    def output(self, text):
        # 输出text到console
        print(text)

    def output_none(self):
        # 不带参数的方法
        print("我不能传入参数")

if __name__ == "__main__":
    # 创建一个类对象
    demo_obj = DemoClass()

    # 调用output
    demo_obj.output("我是参数")

    # 调用output_none
    demo_obj.output_none()
