# __author__ ='wuwa'
# -*- coding:utf-8 -*-
import os
from configparser import ConfigParser


class LYMINIParser:
    def __init__(self, path):
        self.path = path
        self.ini = ConfigParser()
        self.ini.read(self.path)

    def get_sections(self):
        """
        获取section列表
        :return:
        """
        if self.ini:
            return self.ini.sections()

    def get_section_options(self, section):
        """
        获取指定section的option
        :param section:
        :return:
        """
        if self.ini:
            return self.ini.options(section=section)

    def get_section_items(self, section):
        """
        获取指定secion的配置信息列表
        :param section:
        :return:
        """
        if self.ini:
            return self.ini.items(section=section)

    # 按类型读取配置信息

    def get_string(self, section, option):
        """
        返回字符串类型
        :param section:
        :param option:
        :return:
        """
        if self.ini:
            return self.ini.get(section=section, option=option)

    def get_int(self, section, option):
        """
        返回int类型
        :param section:
        :param option:
        :return:
        """
        if self.ini:
            return self.ini.getint(section=section, option=option)

    def get_float(self, section, option):
        """
        返回float类型
        :param section:
        :param option:
        :return:
        """
        if self.ini:
            return self.ini.getfloat(section=section, option=option)

    def get_boolean(self, section, option):
        """
        返回布尔类型
        :param section:
        :param option:
        :return:
        """
        if self.ini:
            return self.ini.getboolean(section=section, option=option)

    def add_sections(self, section):
        """
        添加section
        :param section:
        :return:
        """
        if self.ini:
            self.ini.add_section(section=section)
            self.ini.write(open(self.path, "w"))

    def remove_section(self, section):
        """
        移除section
        :param section:
        :param option:
        :return:
        """
        if self.ini:
            self.ini.remove_section(section=section)
            self.ini.write(open(self.path, "w"))

    def remove_options(self, section, option):
        """
        删除置顶的options
        :param section:
        :param option:
        :return:
        """
        if self.ini:
            self.ini.remove_option(section, option)
            self.ini.write(open(self.path, "w"))

    def set_options(self, section, option, value):
        """
        设置指定的option的值
        :param section:
        :param option:
        :param value:
        :return:
        """
        if self.ini:
            self.ini.set(section=section, option=option, value=value)
            self.ini.write(open(self.path, "w"))


if __name__ == "__main__":
    print("python ini标准库解析实例")

    if os.path.exists("mysql.ini"):
        os.remove("mysql.ini")

    ini = LYMINIParser("mysql.ini")

    # 添加一个mysql_section
    mysql_section = "mysql"
    ini.add_sections(mysql_section)

    # 在mysql_section中写入一些配置信息
    ini.set_options(mysql_section, 'host', '127.0.0.1')
    ini.set_options(mysql_section, 'port', '3306')

    # 在添加一个section

    oracle_section = "oracle"
    ini.add_sections(oracle_section)
    ini.set_options(oracle_section, 'host', '127.0.0.0')

    # 获取所有的section
    sections = ini.get_sections()
    print(sections)

    # 输出每个section下的内容
    for section in sections:
        print('section：', section)
        options = ini.get_section_options(section)
        print(options)

    # 获取option的值
    host = ini.get_string(mysql_section, "host")
    print(host)

    # 删除 section中的option
    ini.remove_section(oracle_section)

    # 删除option的值
    ini.remove_options(mysql_section, 'host')

    # 设置 section的值
    ini.set_options(mysql_section, 'host', '12306')
