#! /usr/bin/env python2
# -*- coding:utf-8 -*-
import configparser

if __name__ == "__main__":
    # 创建一个对象
    config = configparser.ConfigParser()
    # 来让我们写入几组数据
    # 先新增一个section
    config.add_section("开源优测")
    # 在新增的一个section下加key-value键值对
    config.set("开源优测", "微信", "DeepTest")
    config.set("开源优测", "口号", "自我娱乐")
    config.set("开源优测", "号外", "其实有很多公众号")

    # 再新增一个section,但是不加key-value键值对config.add_section("我很好")
    # 写入文件
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)
    # 读文件
    config.read("iniConfig.ini")
    # 获取所有section
    sections = config.sections()
    print(sections)
    # 获取section 下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)
    # 根据sections 和 options 获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s = %s" % (sec, option, config.get(sec, option)))