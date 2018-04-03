#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

for i in range(10):
    if i%2!=0:
        print("--->",i)
        continue
    i+=2
    print(">>>",i)


from  urllib import parse

help(parse)
import urllib.parse



