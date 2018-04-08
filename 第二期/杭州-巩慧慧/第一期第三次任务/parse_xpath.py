#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-21 下午11:18
# @Author  : gonghuihui
# @File    : parse_xpath.py

import xml.etree.ElementTree as ET

# xpath提取或设置指定节点值
# 遍历指定节点
# 读取或设置指定节点的属性
# 新增节点
# 删除节点

class ParseXpath:
    # 提取节点值
    def get_node_text(self, node):
        for child in root.iter(node):
            print(child.text)
            # return child.text

    # 设置节点值
    def set_node_text(self, node, text):
        for child in root.iter(node):
            child.text = text
            child.set('update', 'yes')
            # return 1

    # 读取节点属性值
    def get_node_attrib(self, node):
        for child in root.iter(node):
            print(child.attrib)
            # return child.attrib

    # 设置节点的属性
    def set_node_attrib(self, node, attrib):
        for child in root.iter(node):
            child.attrib = attrib
            # return 1

    # 新增节点
    def add_childnode(self, node, childnode, childnodetext):
        for child in root.iter(node):
            add_childnode = ET.SubElement(child, childnode)
            add_childnode.text = childnodetext
            # print("wx",add_childnode.text)

    # 删除节点，有问题
    def remove_childnode(self, childnode):
        for child in root.findall(childnode):
            print("删除节点", child)
            root.remove(child)


if __name__ == "__main__":

    data = """
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>
    """
    # 从字符串加载xml

    parse_xpath = ParseXpath()
    root = ET.fromstring(data)
    print(root.tag)

    # 遍历根节点下所有子节点及其属性
    # for child in root:
    #     print(child.tag, ":", child.attrib)
    country_attrib = parse_xpath.get_node_attrib("country")

    # 遍历year节点
    # for year in root.iter("year"):
    #     print(year.tag, ":", year.text)
    #     if year.text == "2011":
    #         year.text = "2017"
    #         year.set('update', 'yes')
    #     print("2011->2017",":",year.text)
    year_text = parse_xpath.get_node_text("year")
    update_year_text = parse_xpath.set_node_text("year","2017")

    # 给country新增一个<wx>开元优测</WX>
    # for child in root.iter("country"):
    #     wx = ET.SubElement(child, "wx")
    #     wx.text = "开源优测"
    parse_xpath.add_childnode("country", "wx", "开源优测")


    # 遍历wx节点，并打印
    # for child in root.iter("wx"):
    #     print(child.tag, ":", child.text)
    parse_xpath.get_node_text("wx")

    # 删除节点
    print("---" * 10)
    # for child in root.findall("neighbor"):
    #     root.remove(child)
    parse_xpath.remove_childnode("neighbor")

    # print("---" * 10, root.tag)
    xml_update_data = ET.tostring(root, encoding="unicode")
    # print("xml_update_data", xml_update_data)
    # 操作后保存到xml_write_data.xml
    import codecs
    fp = codecs.open("xml_write_data.xml","w","utf-8")

    fp.write(xml_update_data)

    fp.close()