#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 14:27
# @Author  : yulu
# @File    : file_study
import os

def walk_dir(target_dir):
    # root当前根目录
    # dirs:root下的子目录
    # files:root下的子文件
    walk_result = os.walk(target_dir)
    print(type(walk_result))

    for root, dirs, files in walk_result:
        print(type(root), type(dirs), type(files))
        print("-", root)

        # 遍历当前子目录
        for name in dirs:
            print(" --", name)

        # 遍历当前目录的文件
        for name in files:
            print("--", name)

if __name__ == "__main__":
    # 返回完整的路径信息
    print("获取当前的工作目录")
    print(os.getcwd())

    # 返回的是：相对路径
    print("获取当前目录")
    print(os.curdir)

    # 创建目录
    # 目标创建目录必须是不存在的，否则抛出异常
    os.mkdir("test_mk1")

    # 重命名目录
    os.rename("test_mk1", "test_mk2")

    # 删除指定目录
    # 要注意删除目录必须是无子目录、子文件
    # 删除目录必须存在，否则抛出异常
    # 使用该代码时，请讲目录改为你要删除的目录
    os.removedirs("test_mk2")

    # 将改变至C盘
    print("改变工作目录到dirname")
    # os.chdir("c:")
    # print(os.getcwd())

    # 现初始化当前文件全路径变量
    path = __file__
    print("当前文件全路径为： %s" % path)

    # 是目录，返回True,否则返回False
    print("目录判断：%s" % os.path.isdir(path))

    #判断是否为文件
    print("文件判断：%s" % os.path.isfile(path))

    # 判断目录或文件是否存在
    print("目录/文件存在：%s" % os.path.exists(path))

    # 获取文件大小
    print("文件大小：%s" %os.path.getsize(path))

    # 获取文件绝对路径
    print("文件绝对路径： %s" %os.path.abspath(path))

    # 将目标路径规范化
    print("规范化路径： %s" % os.path.normpath(path))

    # 将文件和目录分割
    # 若传入的是目录，则将最后的目录命做为文件名分割
    print("目录命和文件命分离： ")
    print(os.path.split(path))

    # 分离文件名和扩展名
    print("文件名和扩展名分离：")
    print(os.path.splitext(path))

    # 获取文件命
    print("文件名为：%s" % os.path.basename(path))

    # 获取文件所在目录
    print("文件目录为：%s" % os.path.dirname(path))

    target_dir = os.curdir
    walk_dir(target_dir)