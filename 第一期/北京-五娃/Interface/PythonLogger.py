# __author__ = 'wuwa'
# -*- coding:utf-8 -*-

"""
logging 模块
1、logger 提供日志接口，供应用代码使用，主要是配置、发送日志消息
logging.getLogger(name) 获取logger对象，不指定name则返回root对象
多次使用相同的name调用getLogger方法返回同一个logger对象
2、handler 将日志记录 发送到合适的目的地，比如文件，socket等，
一个logger对象可以通过addHandler方式添加0到N个handler，
每个handler又可以定义不同日志的级别，从而实现日志分级过滤显示
3、filter 绝对是否将日志记录发送到handler
4、formatter 将日志记录输出到具体格式
"""
import logging

LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] \
    %(levelname)s %(message)s'

class Logging:

    def __init__(self,
                 level=logging.DEBUG,  # 日志级别
                 format=LOGGING_FORMAT,  # 日志格式
                 datefmt='%a, %d %b %Y %H:%M:%S',  # 日期格式
                 filename='LYM.log',  # 日志文件名
                 filemode='w'  # 文件打开模式
                 ):
        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode =filemode

        #初始化日志同时输出到控制台和日志文件
        logging.basicConfig(level=self.level,format=self.format,
                            datefmt=self.datefmt,filename=self.filename,
                            filemode=filemode)
        # 定义一个StreamHandler,将INFO级别或者更高的日志信息打印到标准错误中
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s \
            %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('LYMLogger').addHandler(console)
        self.log = logging.getLogger("LYMLogger")

    # 日志输出
    def output(self,msg,level = logging.DEBUG):
        # 调试信息
        if level == logging.DEBUG:
            self.log.debug(msg)
        # 一般信息
        elif level ==logging.INFO:
            self.log.info(msg)
        #警告信息
        elif level == logging.WARNING:
            self.log.warning(msg)
        #错误信息
        elif level ==logging.ERROR:
            self.log.error(msg)
        #其他错误信息
        else:
            self.log.critical(msg)
    def set_level(self,level):
         self.log.setLevel(level=level)

if __name__ =="__main__":
    print("python logging 实例")

    log = Logging()

    log.output("调试信息",level=logging.DEBUG)
    log.output("基本信息",level= logging.INFO)
    log.output("警告信息",level = logging.WARNING)
    log.output("错误信息",level  = logging.ERROR)
    log.output("其他信息", level=logging.CRITICAL)




