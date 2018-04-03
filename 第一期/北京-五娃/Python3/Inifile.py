# __author__ ='wuwa'
# -*- coding: utf-8 -*-
"""
读取：
read(filename) 读取 ini文件内容
sections() 获取所有的section，并以列表的方式返回
options（sections）获取指定section的所有option
get(section,option)huoqu sectionde option的值，返回string类型
写入：
set(section,option,value) 对section中的option进行更新
"""
import configparser as configparser


def create_int():
    """
    创建并写入ini
    :return:
    """
    config = configparser.ConfigParser()
    # 新增一个section
    config.add_section("python3")
    config.set("python3", "dicts", 'dict')
    config.set("python3", "lists", 'list')
    config.set("python3", "tuples", "tuple")

    config.add_section("c++")
    with open("demo.ini", 'w') as configini:
        config.write(configini)


def read_int():
    """
    读取ini
    :return:
    """
    config_read = configparser.ConfigParser()
    config_read.read('demo.ini')
    # 获取所有sections
    sections = config_read.sections()
    print(u'获取所有sections:', sections)

    # 获取所有section下的options
    for sec in sections:
        options = config_read.options(sec)
        print (u'获取每个section下的options:', options)
    # 获取sections下的option下的对应的value
    for sec in sections:
        for option in config_read.options(sec):
            print ("[%s] %s=%s" % (sec, option, config_read.options(sec)))


if __name__ == "__main__":
    create_int()
    read_int()
