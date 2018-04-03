#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


import  pickle

def foo():
    print("ok")



data = pickle.dumps(foo)


print(data)
f = open('PICKLE_text',"wb")

f.write(data)

f.close()
