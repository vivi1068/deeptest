# -*- coding:utf-8 -*-
__author__ = "huohuo"

import os

if __name__ == "__main__":

    # 初始化当前文件全路径变量
    path = __file__
    print("当前文件全路径为: %s " % path)

    # 是目录则返回true否则返回false
    print("目录判断：%s" % os.path.isdir(path))

    # 判断是否是文件
    print("文件判断：%s" % os.path.isfile(path))

    # 判断文件或目录是否存在
    print("存在性判断：%s " % os.path.exists(path))

    # 获取文件大小
    print("文件大小：%s " % os.path.getsize(path))

    # 获取文件绝对路径
    print("文件绝对路径：%s " % os.path.abspath(path))

    # 将目标路径规范化
    print("规范化路径：%s " % os.path.normpath(path))

    # 目录和文件名分割
    print("目录和文件名分割：", end = '')
    print(os.path.split(path))

    # 分离文件名和扩展名
    print("文件名和扩展名分离：", end='')
    print(os.path.splitext(path))

    # 获取文件名
    print("文件名为：%s " % os.path.basename(path))

    # 获取文件所在目录
    print("文件目录为：%s " % os.path.dirname(path))
