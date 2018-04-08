# __author__ ='wuwa'
# -*- coding: utf-8 -*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def read_xml(typevalue, data):
    """
    通过typevalue的值来分辨导入数据类型
    :param typevaue:
    :param data:
    :return:
    """
    if typevalue == 1:
        tree = ET.parse(data)
        root = tree.getroot()
    else:
        root = ET.fromstring(data)
    return root


def nodes_xpath(root, path):
    """
    通过xpath的方式提取
    :param root:
    :param path:
    :return:
    """
    data = root.findall(path)
    for name in data:
        print(name.tag, name.attrib)


def nodes_attrib(root, nodename):
    """
    遍历所有制定节点
    :param root:
    :param nodename:
    :return:
    """
    for child in root.iter(nodename):
        print(child.tag, child.attrib)


def get_all_node(root):
    """
    遍历所有节点
    :param root:
    :return:
    """
    for child in root:
        print(child.tag, child.attrib["name"])


if __name__ == "__main__":
    # 读取文件
    # eg = read_xml(1, 'data_demo_new.xml')

    # 读取字符串方式获取xml内容
    data ="""
    <data>
    <country name="Liechtenstein">
        <rank updated="yes">python3</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">python3</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">python3</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
    """
    eg = read_xml(0, data)

    # 获取节点的name属性
    chlid_node = get_all_node(eg)

    # 指定属性名获取
    chlid_nodes = nodes_attrib(eg, 'country')

    # 通过xpath获取
    nodes_xpath(eg, '.')
    nodes_xpath(eg, './/country')
    nodes_xpath(eg, './/*[@name="Panama"]')
