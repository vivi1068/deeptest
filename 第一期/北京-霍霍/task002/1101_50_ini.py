# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 导入模块

import configparser

if __name__ == "__main__":
    # 先构建一个对象
    config = configparser.ConfigParser()

    # 写入数据
    # 先新增一个section
    config.add_section("开源优测")

    # 在新增的section下加key-value键值对
    config.set("开源优测", "微号", "DeepTest")
    config.set("开源优测", "口号","自我娱乐")
    config.set("开源优测", "号外","其实有好号")

    # 再新增一个section，但是不加key-value键值对
    config.add_section("动力源")
    # 写入文件
    with open("iniConfig.ini", 'w') as configfile:
        config.write(configfile)

    ####################################

    # 读取ini文件
    config.read("iniConfig.ini")
    # 获取所有的section
    sections = config.sections()
    print(sections)

    # 获取section下的options
    for sec in sections:
        options = config.options(sec)
        print(options)

    # 根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[ %s ] %s = %s " % (sec, option, config.get(sec, option)))