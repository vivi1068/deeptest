__author__='棒棒糖'
try:
    import xml.etree.ElementTree as ET
except ImportError:
    import  xml.etree.ElementTree as ET
if __name__=='__main__':
    print('Element Tree XPath特性支持示例')
    #加载xml文件
    tree=ET.parse('data.xml')
    #获取根节点，并打印文本students
    root=tree.getroot()
    #选择当前节点, 返回的是当前节点对象列表
    print('选择当前节点')
    data=root.findall('.')
    for d in data:
        print(d.tag)
    # 选择所有student节点
    print('选择所有country节点方法一')
    student=root.findall('.//student')
    for x in student:
        print(x.tag,'',x.attrib['no'])
    print('选择所有country节点方法二')
    student=root.findall('student')
    for x in student:
        print(x.tag,'',x.attrib['no'])
    print('选择no属性为2009081097的student节点')
    student=root.findall('.//*[@no="2009081097"]')
    for x in student:
        print(x.tag,'',x.attrib['no'])
    print('选择no属性为2009081097的student下的age')
    age=root.findall('.//*[@no="2009081097"]/age')
    for x in age:
        print(x.text)
    # 通过索引来选择student节点，选择第一个student节点
    # 注意索引从 1 开始
    print("通过索引来选择student节点，选择第一个student节点")
    student=root.findall('.//student[1]')
    for x in student:
        print(x.tag, '', x.attrib['no'])
    # 通过子节点的文本内容来选择节点
    # 选择子节点age且其文本为19 的student节点
    # 请注意这返回的是age的父节点
    print("通过子节点的文本内容来选择节点")
    age=root.findall('.//*[age="19"]')
    for x in age:
        print(x.tag)
