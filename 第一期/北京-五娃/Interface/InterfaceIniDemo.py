# __author__ ='wuwa'
# -*- coding:utf-8 -*-

import configparser

from os import path

"""
1、INI文件格式
[section]
key=value
;英文分号注释
key1=value1
2、通过ConfigParser进行ini文件的读写
"""

# 初始化
cf =configparser.ConfigParser()
cf.read(path)
# 获取所有sections
sections = cf.sections

# 获取指定的section
options = cf.options("mysql")
print(options)

# 获取指定section中的配置信息
host = cf.get("mysql","host")
print(host)
# 设置某个option的值并保存
cf.set("mysql","passwd","123456")
# 添加section并保存
cf.add_section("python")
cf.set('python', 'pytho1', '127.0.0.1')
cf.set('python', 'po1rt', '5555')
# 移除section或者option并保存
cf.remove_option('python','po1rt')
cf.remove_section('python')
