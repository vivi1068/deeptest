
#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")




import  pickle

def foo():
    print("ok")

f= open('PICKLE_text','rb')


data =f.read()

data = pickle.loads(data)

data()
# print(data['name'])
