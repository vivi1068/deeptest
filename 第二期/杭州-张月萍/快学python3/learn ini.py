# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import configparser

if __name__ == "__main__":
    # 先构建一个对象
    config = configparser.ConfigParser()

    # 新增一个section
    config.add_section("开源优测")

    # 在新增的section下加key-valus键值对
    config.set("开源优测", "微信号", "Deeptest")
    config.set("开源优测", "微号", "Deep")
    config.set("开源优测", "信号", "test")

    # 再新增一个section，但不加key-valus键值对
    config.add_section("我好孤单")
    # 写入文件
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)

    # 读取ini文件
    config.read("iniConfig.ini")
    # 获取它的所有section
    sections = config.sections()
    print(sections)

    # 获取section下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)

    # 根据sections和options获取对应的value值
    for sec in sections:
        for options in config.options(sec):
            print("[%s] %s=%s" % (sec, options, config.get(sec, options)))
