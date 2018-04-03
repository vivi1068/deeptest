# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
os和path模块常用方法说明
os模块目录遍历方法walk
"""
import os


def walk_dir(dir):
    walk_result = os.walk(dir)
    print (type(walk_result))
    for root, dirs, files in walk_result:
        print (type(root))
        print (type(dirs))
        print (type(files))
        # 打印根目录
        print ('-', root)
        # 打印子目录
        for name in dirs:
            print('--', name)
        for name in files:
            print ('--', name)



if __name__ == "__main__":
    print ("获取当前工作目录")
    print (os.getcwd())

    print ("获取当前目录")
    print (os.curdir)

    print ("创建目录")
    os.mkdir("test_mk1")

    print ("重命名目录")
    os.rename("test_mk1", "test_mk")

    # 删除的目录必需无子目录以及子文件
    # 删除目录必需存在，否则抛出异常
    print ("删除指定的目录")
    os.removedirs("test_mk")

    path = __file__
    print ("当前py文件全路径为：%s" % path)

    print ("目录判断:", os.path.isdir(path))

    print ('文件判断', os.path.isfile(path))

    print("判断目录/文件存在", os.path.exists(path))

    print ("文件大小", os.path.getsize(path))

    print ("文件绝对路径", os.path.abspath(path))

    print("规范化路径: %s" % os.path.normpath(path))

    # 将文件名和目录分割
    # 若传入的是目录，则将最后的目录名做为文件名分割
    print("目录和文件名分割：")
    print(os.path.split(path))

    # 分离文件名和扩展名
    print("文件名和扩展名分离：")
    print(os.path.splitext(path))

    # 获取文件名
    print("文件名为：%s" % os.path.basename(path))

    # 获取文件所在目录
    print("文件目录为：%s" % os.path.dirname(path))
    print ("-----------分割线-----------")
    target_dir = os.curdir
    walk_dir(target_dir)