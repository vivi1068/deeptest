#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 19:32
# @Author  : yulu
# @File    : xpath_study
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == "__main__":
    print("Element Tree Xpath特性支持事例")

    # 加载
    tree = ET.parse("data_demo.xml")

    # 获取根节点并打印
    root = tree.getroot()

    print("选择当前借点")
    data = root.findall(".")
    for d in data:
        print(d.tag)

    # 选择所有country节点
    print("选择所有country节点")
    countries = root.findall(".//country")
    for country in countries:
        print(country.tag, ":", country.attrib["name"])

    # 选择所有country节点，另一种方法
    print("选择所有country节点")
    countries = root.findall(".//country")
    for country in countries:
        print(country.tag, ":", country.attrib["name"])

    print("选择name属性为Panama的country节点")
    for country in root.findall(".//*[@name='Panama']"):
        print(country.tag, ":" ,country.attrib["name"])

    print("name属性为Panama的country下的year节点")
    years = root.findall(".//country[@name='Panama']/year")
    for year in years:
        print(year.text)

    print("通过索引来选择country节点，选择第一个country节点")
    country = root.findall(".//country[1]")
    print(country)
    for c in country:
        print(c.tag, ":", c.attrib["name"])

    # 通过子节点的文本来选择节点
    print("通过子节点的文本来选择节点")
    gdppc = root.findall(".//*[gdppc='59900']")
    for gd in gdppc:
        print(gd.tag)
