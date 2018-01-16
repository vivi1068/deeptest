# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import configparser

if __name__ == "__main__":
    #先构建一个对象
    config = configparser.ConfigParser()

    # 来让我们写入几组数据
    # 先新增一个section
    config.add_section("开源优测")

    # 在新增的section下加key-value键值对
    config.set("开源优测","微信公众号", "DeepTest")
    config.set("开源优测", "口号", "自娱自乐")
    config.set("开源优测", "号外", "其实我开了好多号")

    #再新增一个section，但不加key-value键值对
    config.add_section("另一个section")

    # 写入文件
    with open('initconfig.ini', 'w') as configfile:
        config.write(configfile)


###################################################
    # 下面开始我们来把刚才的ini文件读出来看看
    config.read("initconfig.ini", "gbk")
    sections = config.sections()
    print(sections)

    #获取section下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)

    # 根据sections和options获取对应的value值
    for sec in sections:
        for opt in config.options(sec):
            print("[%s] %s=%s " %(sec, opt, config.get(sec, opt)))