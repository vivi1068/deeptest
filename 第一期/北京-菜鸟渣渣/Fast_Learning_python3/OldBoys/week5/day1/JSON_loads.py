#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

import  json

f= open('JSON_text','r')


# data =f.read()
#
# data = json.loads(data)

data = json.load(f )


print(data['name'])


