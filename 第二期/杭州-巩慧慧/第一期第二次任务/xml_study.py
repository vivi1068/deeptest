#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 12:34
# @Author  : yulu
# @File    : xml_study
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree

if __name__ == "__main__":
    print("解析本地的data_demo.xml")
    # 加载xml文件
    tree = ET.parse("data_demo.xml")

    # 获取根节点，打印借点文本：data
    root = tree.getroot()
    print(root.tag)

    # 遍历输出 country及其name属性
    for child in root:
        print(child.tag, "name：", child.attrib["name"])

    # 遍历rank节点
    # 借助iter迭代器的特性来进行全迭代查找感兴趣的节点
    # 输出借点及其文本
    for rank in root.iter("rank"):
        print(rank.tag, "-", rank.text)
        # print(rank)

    # 借助findall来找rank
    for country in root.findall("country"):
        rank = country.findall("rank")
        for r in rank:
           print(rank.tag, "-", rank.text)

    # 把所有的rank文本修改为：开源优测
    for rank in root.iter("rank"):
        rank.text = "开源优测"
        rank.set('update', 'yes')

    for rank in root.iter("rank"):
        print(rank.tag, "-", rank.text)

    # 增加节点
    for country in root.iter("country"):
        # 创建借点
        url = ET.Element("url")
        # 赋值
        url.text = "www.testingunion.com"
        # 将url借点追加到country下面
        country.append(url)

    # 打印整个xml
    for country in root.iter("country"):
        url = country.find("url")
        print(url.text)

    # 删除year节点
    for country in root.iter("country"):
        year = country.find("year")

        if year is not None:
            print("删除了一个year借点")
            country.remove(year)

    # 保存到文件
    tree.write("data_demo_new.xml", encoding="utf-8")