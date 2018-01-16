__author__ = '棒棒糖'

try:
    # 若想加快速度，可以使用C语言编译的API xml.etree.cElementTree。
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

print('解析本地xml文件')
# 加载xml文件
tree = ET.parse("data.xml")
# 获取根节点，并打印节点文本：students
root = tree.getroot()
print(root.tag)
# 遍历输出student及其no"属性
for child in root:
    print(child.tag, "no：" ,child.attrib["no"])
 # 遍历rank节点
# 我们借助iter迭代器来进行全迭代查找感兴趣的节点
# 输出节点tag及其文本
print('使用iter迭代器查找目标节点 ')
for name in root.iter('name'):
    print(name.tag,'-',name.text)
        # 换一种方式来遍历rank节点
        # 我们借助findall和find方法来查找感兴趣的节点
        # 输出节点tag及其文本
        # 注意：findall只能查找从当前节点的子节点查找目标节点
print('使用findall查找目标节点')
#使用findall查找所有student节点，用于遍历
for student in root.findall('student'):
    #使用find从student节点中查找name节点
    name=student.find('name')
    print(name.tag, '-', name.text)
#把所有的name的文本都修改为： 棒棒糖
for name in root.iter('name'):
    name.text='棒棒糖'
    name.set('updated','yes')
#打印修改后的文本
for name in root.iter('name'):
    print(name.text)
#给所有的student新增一个<url>www.testingunion.com</url>节点
for student in root.iter('student'):
    #创造一个节点
    url=ET.Element('url')
    #给节点赋值
    url.text='www.testingunion.com'
    #将url节点追加到student节点下
    student.append(url)
# 打印下整个xml出来看看是不是所有student节点都新增了一个url节点
for student in root.iter('student'):
    #查找url节点
    url=student.find('url')
    #打印url的text
    print(url.text)
#删除year节点
for student in root.iter('student'):
    gender=student.find('gender')
    #如果gender节点存在，则删除
    if gender is not None:
        print('删除一个gender节点')
        student.remove(gender)

tree.write("data_demo_new1.xml", encoding="utf-8")