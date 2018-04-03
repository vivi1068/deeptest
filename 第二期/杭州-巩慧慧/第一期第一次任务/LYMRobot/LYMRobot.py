#-*- coding:utf-8 -*-

import unittest
import os
import time
from pathlib import Path

__author__ = "苦叶子"

LOG_PATH = os.path.normpath(os.path.dirname(__file__) + time.strftime("\\logs\\%Y-%m-%d.log", time.localtime()))

if __name__ == "__main__":
    
    print("LYMRobot start...")

    print("关注公众号: 开源优测")

    if not os.path.exists(LOG_PATH):
        print("创建日志文件...")
        Path(LOG_PATH).touch()

    print("加载测试用例...")
    case_dir = os.path.normpath(os.path.dirname(__file__) + "\\testcase")
    print(case_dir)
    
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py",top_level_dir=None)
    print(discover)
    
    print("执行测试用来...")
    runner = unittest.TextTestRunner()
    runner.run(discover)
