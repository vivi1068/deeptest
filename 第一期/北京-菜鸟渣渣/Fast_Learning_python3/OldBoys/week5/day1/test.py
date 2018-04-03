#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")



# dic = str({'1':'11'})
#
# f = open('test','w')
#
# f.write(dic)
#


f =open('test','r')
dic = f.read()

print(eval(dic)['1'])

####序列化
