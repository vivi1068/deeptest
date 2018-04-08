#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

import sys

print(sys.path)


from  calls import add as plus




def sub(a,b):
    return a-b


print(sub(5,2))
print(plus(12,3))

