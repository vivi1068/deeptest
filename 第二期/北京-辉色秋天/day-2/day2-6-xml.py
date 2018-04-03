#-*-coding:utf-8-*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etrre.ElementTree as ET


def etree_t():
    print("解析本地data_demo.xml")
    tree = ET.parse("data_demo.xml") 
    root = tree.getroot()
    print(root.tag)


    for i in root:
        print(i.tag,i.attrib['name'])

    print("使用iter迭代器查找目标节点")
    for rank in root.iter("rank"):
        print(rank.tag,rank.text)

    print("使用findall查找目标节点")
    for i in root.findall("country"):
            j = i.find("rank")
            print(j.tag, j.text)

    for rank in root.iter("rank"):
        rank.text="我被修改了"
        rank.set("updated", 'yes')

    for rank in root.iter("rank"):
        print(rank.text)  

    for country in root.findall("country"):
        url = ET.Element("url")
        url.text ='www.baidu.com'
        country.append(url)
 
    for country in root.findall('country'):
        url = country.find("url")
        print(url.text)


    for country in root.iter('country'):
        year = country.find("year")
        if year is not None:
            country.remove(year)

    tree.write("data_demo-1.xml",encoding='utf-8')
    
def xpath1():
    print("Element Tree XPath特性支持示例")    

    tree = ET.parse("data_demo.xml")
    
    root = tree.getroot()

    data = root.findall('.')
    for i in data:
        print(i.tag)


    """
    此方法适用于任意节点
    """
    neighbors = root.findall(".//neighbor")
    for neighbor in neighbors:
        print(neighbor.tag, neighbor.attrib['name'])



    """
    此方法只适合于查找直系子节点
    """
    countrys = root.findall("country")
    for country in countrys:
        print(country.tag, country.attrib['name'])

    """ *[@name='Panama'] 等号周围不能有空格""" 
    print("选择name属性为Panama的country节点")
    countrys = root.findall(".//*[@name='Panama']")
    for country in countrys:
        print(country.tag, country.attrib['name'])  

    years = root.findall(".//country[@name='Panama']/year")
    for year in years:
        print(year.tag, year.text)


    print("通过索引来选择country节点，选择第一个country节点")
    countrys = root.findall(".//country[1]")
    for country in countrys:
        print(country.tag, country.attrib['name'])

    print("通过子节点的文本内容来选择节点")
    gdppcs = root.findall(".//*[gdppc='59900']")
    for gdppc in gdppcs:
        print(gdppc.tag)
if __name__ == "__main__":
    xpath1()
