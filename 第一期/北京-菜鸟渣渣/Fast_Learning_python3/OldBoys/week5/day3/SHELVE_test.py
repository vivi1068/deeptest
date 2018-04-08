#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

import shelve

# f = shelve.open(r"SHELVE_text")
#



f = shelve.open("SHELVE_text")

# f['info'] ={"name":'alex',"age":"18"}
# f['info'] ={"name":'alex',"age":"18"}
# f['shopping'] ={"name":'alex',"price":"-0001000"}
#
# print(f.get('info'))

d= {"name":'alex',"age":"18"}
# d['name'] ='aa'
print(d.get('name'))


print(d.get("sex" ,'male'))



