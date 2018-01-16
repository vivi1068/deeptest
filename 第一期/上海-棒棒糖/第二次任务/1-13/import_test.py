#模块导入方式
#第一种
import sys
#第二种
from sys import path

'''
#包的示例
autoTest/  #顶层包
    __init__.py  #初始化autoTest包
    log/
        __init__.py
        htmlLogger.py
        xmlLogger.py
        ...
    formats/   #文件解析器子包
        __init__.py
        excelParser.py
        xmlParser.py
        htmlParser.py
        ...
    driver/    #自动化测试驱动包
        __init__.py
        wbDrier.py
        httpDriver.py
        ...
    ...
auto.py   #main入口       
'''
__author__='棒棒糖'
from autoTest.driver import wbDriver
#如果wbDriver.py中有wbDriver类，那么可以这样导入
from autoTest.driver.wbDriver import wbDrver
if __name__=='__main__':
    pass