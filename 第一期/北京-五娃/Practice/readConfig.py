# __author__ ='wuwa'
# -*- coding: utf-8 -*-

import os
import configparser

# 获取当前文件的上级目录
proDir = os.path.abspath(os.path.dirname(os.getcwd()))
# 获取ini文件的路径
configPath = os.path.join(proDir, "config\config.ini")


class ReadConfig:
    """
    获取指定section的key的值
    """

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_config_value(self, types, name):
        return self.cf.get(types, name)


if __name__ == "__main__":
    demo = ReadConfig()
    value = demo.get_config_value('HTTP', 'baseurl')
    print(value)
