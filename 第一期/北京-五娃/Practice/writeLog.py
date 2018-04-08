# __author__ ='wuwa'
# -*- coding: utf-8 -*-

import logging, time, os

from common import readConfig


class MyLogging:
    '''
    logging的初始化操作，以类封装的形式进行
    '''

    def __init__(self):
        # 获取当前文件的上级目录
        DIR = readConfig.BASE_DIR
        # 在当前目录的上级目录添加logs目录
        resultPath = os.path.join(DIR, "logs")
        # 如果不存在logs目录则添加logs
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs'))
        # 日志文件的地址
        filename = lib_path + '/' + timestr + '.log'
        # 定义对应的程序模块名name，默认为root
        self.logger = logging.getLogger()
        # 必须设置，这里如果不显示设置，默认过滤掉warning之前的所有级别的信息
        self.logger.setLevel(logging.INFO)

        # 日志输出到屏幕控制台
        sh = logging.StreamHandler()
        # 设置日志等级
        sh.setLevel(logging.ERROR)
        # 向文件filename输出日志信息
        fh = logging.FileHandler(filename=filename)
        # 设置日志等级
        fh.setLevel(logging.INFO)

        # 设置格式对象 定义日志输出格式
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")

        # 设置handler的格式对象
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 将handler增加到logger中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


mylogger = MyLogging().logger

if __name__ == "__main__":
    mylogger = MyLogging().logger

    mylogger.debug("debug")
    mylogger.info("info")
    mylogger.warning("warning")
    mylogger.error("error")
    mylogger.critical("critical")
