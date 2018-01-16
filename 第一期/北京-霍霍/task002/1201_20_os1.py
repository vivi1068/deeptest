# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 导入os模块
import os

if __name__ == "__main__":
    # 返回完整的路径目录
    print("获取当前工作目录")
    print(os.getcwd())

    # 返回的是：
    print("获取当前目录")
    print(os.curdir)

    # 创建目录
    os.mkdir("test_mk1")

    #重新命名
    os.rename("test_mk1", "test_mk2")

    # 删除目录
    os.removedirs("test_mk2")
