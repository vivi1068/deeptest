# -*- coding utf-8 -*-
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    # 先新增一个section
    config.add_section('中国')
    # 在新增的section下新增key-value对
    config.set('中国', '河北', '石家庄')
    config.set('中国', '河南', '郑州')
    config.set('中国', '山东', '济南')
    # 再新增一个section，但是不增加键值对
    config.add_section('民国')
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)

        ##########################################
        # 读取ini文件
    config.read('iniConfig.ini')
    # 获取所有的section
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
