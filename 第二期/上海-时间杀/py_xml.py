#!usr/bin/python3
# -*- coding:utf-8 -*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 解析xml文件 增删改读

# 加载xml文件
tree = ET.parse("data_demo.xml")
root = tree.getroot() # 获取根节点
# print(type(root))

for child in root:
    print(child.tag, "name:", child.attrib["name"])
    # print(child.attrib, "tail:", child.tail)

print(root.attrib, "tail:", root.tail) # attrib是dict对象

# Element类和ElementTree类都有iter()方法可以递归遍历元素/树的所有子元素
for rank in root.iter("rank"):
    print(rank.tag, rank.text)

"""
# 全遍历
for sodo in root.iter():
    print(sodo.tag, "attributes:", sodo.attrib, "text:", sodo.text)
"""

# 查找节点
for country in root.findall("country"): # 返回所有匹配的元素或None
    print(type(country))
    rank = country.findall("neighbor") # findall返回的是list find只返回第1条
    print(rank[0].tag, rank[0].text)
    """
    try:
        print(rank[1].tag, rank[1].text)
    except:
        pass
    """
"""
# 修改 添加 删除
for rank in root.iter("rank"):  # 必须使用这种循环的方式增删改查
    print(type(rank))
    rank.set('update', 'yes')   # 添加新的attrib
    rank.text = str(int(rank.text) + 1)

for cou in root:
    co = cou.attrib["name"]
    if co == "Singapore":
        url = ET.Element("url")
        url.text = "www.baidu.com"
        cou.append(url)

    coo = cou.find("year")
    cooo = int(coo.text)
    if cooo == 2008:
        cou.remove(coo)
    

tree.write("data_demo_new.xml", encoding="utf-8")
"""

# XPATH特性支持
# 选择当前节点  返回的是当前节点对象列表
data2 = root.find(".")
for d in data2:
    print(d.tag)

# 查找指定节点
cou = root.findall(".//country")
print(type(cou))
print(cou[0].tag, cou[0].attrib["name"])

cou1 = root.findall(".//*[@name='Singapore']")
print(cou1[0].tag)  # 哪怕只有1个也得加[*]

cou2 = cou1[0].find("./year")
# cou2 = root.find(".//*[@name='Singapore']/year")
print(cou2.text)

# 通过索引来选择第X个节点
cout = root.findall(".//country[1]")
for i in cout:
    print(i.tag, i.attrib["name"])

# 通过子节点的文本内容来选择节点
cou3 = root.findall(".//*[gdppc='19900']")
for d in cou3:
    print(d.tag)    # 选择的是父节点
