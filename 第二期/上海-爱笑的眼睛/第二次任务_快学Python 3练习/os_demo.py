# -*- coding:utf-8 -*-
#__author__ = 'smile eyes'

# 导入os模块
import os

if __name__ == "__main__":    
    # 返回完整的路径目录
    print("获取当前工作目录")    
    print(os.getcwd())    

    # 返回的是: .
    print("获取当前目录")    
    print(os.curdir)    
    
    # 创建目录
    # 目标创建目录必须是不存在的，否则抛出异常
    os.mkdir("test_mk1")    

    # 重命名目录
    os.rename("test_mk1", "test_mk2")    

    # 删除指定目录
    # 要注意目标删除目录必须是无子目录、子文件
    # 目标删除目录必须存在，否则抛出异常
    # 使用该代码时，请将目标删除目录改为你要删除的目录
    # os.removedirs("test_mk1")

    # 将改变至C盘
    print("改变工作目录到dirname")
    os.chdir("c:")    
    print(os.getcwd())