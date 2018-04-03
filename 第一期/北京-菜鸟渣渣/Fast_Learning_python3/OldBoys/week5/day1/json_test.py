#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


#
import  json
#

# def foo():
#     print("ok")
#
#
#
# data = json.dumps(foo)

# f = open('JSON_text',"w")
#
# f.write(data)
#
# f.close()
# #




# dic = {"name":'alex',"age":"18"}
#
# data = json.dumps(dic)
#
# f = open('JSON_text',"w")
#
# f.write(data)
#
# f.close()
#

###############dump

dic = {"name":'alex',"age":"18"}

# data = json.dumps(dic)
# f.write(data)

f = open('JSON_text2',"w")

json.dump(dic,f)



f.close()

