#!/usr/bin/python
#encoding=utf-8

__author__='小白龙'

import configparser

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
    print(ini.getSections())
    print(ini.getOptions('chengji'))
    print(ini.getAllOptions())
    print(ini.getValues('chengji'))