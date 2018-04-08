#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


import sys
print(sys.path)

sys.path.append("F:\\user\Young\\Fast_Learning_python3\\OldBoys\day8\\模块项目")

from moudle import  logger

logger.fun()

print(__file__)

import  os

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))