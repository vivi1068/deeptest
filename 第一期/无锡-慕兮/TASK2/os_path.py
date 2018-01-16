# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import os

if __name__ == "__main__":
    # 先初始化当前文件全路径变量
    path = __file__
    print("当前文件全路径为：%s" %path)

    #是目录就返回True，否则返回False
    print("目录判断：%s"%os.path.isdir(path))

    # 判断是否为文件，是则返回True，否则返回False
    print("文件判断：%s"%os.path.isfile(path))

    # 判断目录或文件是否存在
    print("文件是否存在：%s"%os.path.exists(path))

    # 获取文件大小，若目标为目录则返回0
    print("文件大小：%s"%os.path.getsize(path))

    # 获取文件的绝对路径
    print("文件的绝对路径：%s"%os.path.abspath(path))

    #将目标路径规范化， 即更规范的路径表达方式，跨平台标识
    print("规范化路径: %s" %os.path.normpath(path))

    #将文件名和目录分割
    # 若传入的是目录，则将最后的目录名做为文件名分割
    print("目录文件名分割", end = " ")
    print(os.path.split(path))

    #分离文件名和扩展名
    print("分离文件名和扩展名", end=" ")
    print(os.path.splitext(path))

    # 获取文件名
    print("文件名：%s"%os.path.basename(path))

    # 获取文件所在目录
    print("文件所在目录：%s"%os.path.dirname(path))
