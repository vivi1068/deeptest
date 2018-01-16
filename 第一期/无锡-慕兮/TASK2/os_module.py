# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

#导入os 模块
import os

if __name__ == "__main__":
    # 返回完整的路径目录
    print("获取当前工作目录：", os.getcwd())

    #返回的是.
    print("获取当前目录", os.curdir)

    #创建目录
    os.mkdir("py")

    #重命名目录
    os.rename("py", "python")

    # 删除指定目录
    # 要注意目标删除目录必须是无子目录、子文件
    # 目标删除目录必须存在，否则抛出异常
    # 使用该代码时，请将目标删除目录改为你要删除的目录
    os.removedirs("python")

    #改变当前目录
    os.chdir("c:/")
    print(os.getcwd())