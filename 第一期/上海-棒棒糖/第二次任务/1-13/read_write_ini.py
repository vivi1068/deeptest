'''
ini是常见到的配置文件格式之一
组成格式：option就是key
[section_1]
key1 = value1
key2 = value2
key3 = value3
key4 = value4

[section_2]
key1 = value1
key2 = value2
key3 = value3
key4 = value4
ConfigParser模块来对ini文件进行读写操作
读取

read(filename) 读取ini文件内容
sections() 获取所有的section，并以列表的形式返回
options(sections) 获取指定section的所有option
get(section,option) 获取section中value的值，返回为string类型
写入

set( section, option, value) 对section中的option进行更新
'''
import  configparser
#构建对象
config=configparser.ConfigParser()
#写入数据，新增一个section
config.add_section('棒棒糖')
#在新增的section中加入key-valve键值对
config.set('棒棒糖','微号','DeepTest')
config.set('棒棒糖','口号','碰一个')
config.set('棒棒糖','号外','碰一个不要钱')
#在新增一个section，不加入key-valve键值对
config.add_section('甜甜圈')
#写入文件
with open('iniConfig.ini','w') as conmgfigfile:
    config.write(conmgfigfile)
#读取iniConfig.ini
config.read('iniConfig.ini')
#获取所有section
sections=config.sections()
print(sections)
#用options获取section下所有key
for sec in sections:
    key=config.options(sec)
    print(key)
#根据sections和options获取对应的value值
for sec in sections:
    for option in config.options(sec):
        print('[%s]%s=%s'%(sec,option,config.get(sec,option)))


