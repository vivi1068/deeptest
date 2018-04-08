#!/usr/bin/python
#encoding=utf-8

__author__='小白龙'

import configparser
import os
from os import path

class INIHander:
    def __init__(self,path,name):
        self.path = path
        self.name = name
        filepath = path+'\\'+name
        self.config = configparser.ConfigParser()
        with open(filepath,'w') as configfile:
            self.config.write(configfile)
        print(u'在"%s"目录下新建%s文件'%(path,name))

    def addSection(self,section):
        self.config.add_section(section)

    def getSections(self):
        sec = self.config.sections()
        return sec

    def addOption(self,section,option,value):
        self.config.set(section,option,value)
    def updateOption(self,section,option,value):
        self.config.set(section, option, value)
    def getOptions(self, section):
        opts = self.config.options(section)
        return opts
    #获取整个文件的所有的option
    def getAllOptions(self):
        sections = self.config.sections()
        list = []
        for sec in sections:
            list.append(self.config.options(sec))
        return list
    def getValue(self,section,option):
        value = self.config.get(section.option)
        return value
    #获取section下的所有option及对应的value
    def getValues(self,section):
        dic = {}
        for opt in self.config.options(section):
            dic.setdefault(opt,self.config.get(section,opt))
        return dic

if __name__=='__main__':
    ini =  INIHander(u'D:\GitHub\deeptest\第二期\上海-小白龙\第二次任务','testini')
    ini.addSection('infomation')
    ini.addOption('infomation','姓名','小白龙')
    ini.addOption('infomation', '身高', '180')
    ini.addOption('infomation', '身价', '18个亿')
    ini.addSection('chengji')
    ini.addOption('chengji', '语文', '41')
    ini.addOption('chengji', '数学', '38')
    ini.addOption('chengji', '英语', '5')
    ini.updateOption('chengji', '英语', '11')
    print(ini.getSections())
    print(ini.getOptions('chengji'))
    print(ini.getAllOptions())
    print(ini.getValues('chengji'))

    cwd = os.getcwd()
    print(u'当前路径：%s'%cwd)
    os.mkdir('test_dir1',7)

    print(u'新建文件夹：test_dir1' )
    dir2= os.rename('test_dir1','test_dir2')
    print(u'重命名文件夹：test_dir2' )
    os.removedirs('test_dir2')
    os.chdir('D:\GitHub')
    print(os.getcwd())

    #path = os.getcwd()
    path = __file__
    print("当前文件全路径为： %s" % path)
    print(u'是否是目录：%s'%os.path.isdir(path))
    print(u'是否是文件：%s' % os.path.isfile(path))
    print(u'是否存在：%s' % os.path.exists(path))
    print(u'文件大小：%s'%os.path.getsize(path))
    print('文件绝对路径：%s'%os.path.abspath(path))
    print('文件规范化路径：%s'%os.path.normpath(path))
    print("目录和文件名分割：", end="")
    print(os.path.split(path))
    print("文件名和扩展名分离：", end="")
    print(os.path.splitext(path))
    print("文件名为：%s" % os.path.basename(path))
    print("文件目录为：%s" % os.path.dirname(path))


    """walk返回值说明： 返回值为一个迭代器对象，它的每个部分包含一个元组，
    即(目录X, [目录X下的目录列表], [目录X下的文件列表]),注：包括所有的子目录以及子文件"""
    def walkFiles(path):
        result_tup = os.walk(path)
        for root,dirs,files in result_tup:
            print('目录：%s'%root)
            for dir in dirs:
                print('文件夹：%s'%dir)
            for file in files:
                print('文件：%s'%file)

    walkFiles(u'D:/GitHub/deeptest/第二期/上海-小白龙/')

    def dir_tree(dir_path):
        if not os.path.isdir(dir_path):
            print("%s是非法目录" % (dir_path))
            return False
        for name in os.listdir(dir_path):
            fullpath = os.path.join(dir_path, name)
            print(fullpath)
            if os.path.isdir(fullpath):
                dir_tree(fullpath)

    print('=================================')
    a = r"D:/GitHub/deeptest/第二期/上海-小白龙/"
    dir_tree(a)