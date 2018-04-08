#-*-coding:utf-8-*-
import os

def os_test():

    print("输入当前目录,完整路径")
    print(os.getcwd())

    print("当前工作目录")
    print(os.curdir)

    print(os.listdir("/root"))
    print("*********************************")
    os.mkdir("/root/1111")
    print(os.listdir("/root"))
    os.rename("/root/1111",'/root/aaaa')
    print("*********************************")
    print(os.listdir("/root"))
    print("*********************************")
    os.rmdir("/root/aaaa")
    print(os.listdir("/root"))
    print("*********************************")

    print('更改目录到root下')
    os.chdir("/root")
    print(os.getcwd())


def path_test():
    path = __file__
    print("当前文件路径：%s"%path)

    print("/root/test1.py 是否是文件：%s"%str(os.path.isfile("/root/test1.py")))
    print("/root 是否是文件：%s"%(os.path.isfile("/root")))
    print("/root/test3333.py 是否是文件：%s"%str(os.path.isfile("/root/test33333.py")))

    print("/root/test1.py 是否是目录：%s"%str(os.path.isdir("/root/test1.py")))
    print("/root 是否是目录：%s"%(os.path.isdir("/root")))
    
    print("__file__ = "+path)
    print("__file__绝对路径"+os.path.abspath(path))
    
    print("__file__ size is "+str(os.path.getsize(path)))
    print("normpath  is "+str(os.path.normpath(path)))

    print("目录和文件分割："+str(os.path.split("/root/test1.py")))
    print("后缀分离"+str(os.path.splitext("/root/test1.py")))
    print("文件名"+str(os.path.basename("/root/test1.py")))
    print("所在目录"+str(os.path.dirname("/root/test1.py")))
    
def walk_dir(path):
    walk_result = os.walk(path)
    for root, dirs,files in walk_result:
        print("-",root)
        for name in dirs:
            print("-",name)
        for name in files:
            print('-',name)

if __name__ == "__main__":
    
    #path_test()
    walk_dir("/data")
