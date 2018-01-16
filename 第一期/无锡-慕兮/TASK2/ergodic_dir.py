# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import os

def walk_dir(target_dir):
    # root：当前根目录
    # dirs：root下的子目录
    # files： root下的子文件
    walk_result = os.walk(target_dir)
    print(type(walk_result))

    for root, dirs, files in walk_result:
        print(type(root), type(dirs), type(files))
        print("-", root)
        for name in dirs:
            print(" --", name)

        for name in files:
            print(" --", name)

if __name__ == "__main__":
    target_dir = os.getcwd()
    walk_dir(target_dir)