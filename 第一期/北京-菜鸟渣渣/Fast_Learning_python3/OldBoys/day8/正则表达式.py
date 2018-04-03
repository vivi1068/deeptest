#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


#字符串提供的方法是完全匹配

# s = "hello world"

#引入正则

import re

# ret = re.findall('w\w{2}l',"hello world")
# print(ret)
# . 可以代表所有的字符 . 就是不能代表换行符
# ret=re.findall('w..l', 'hello world') #. 只能代指任意一个字符
# print(ret)


# ret=re.findall('w..l', 'hello w\nld')
# print(ret)
# 元字符

# .  通配符
# ret=re.findall('w..l', 'hello w\t ld')
# print(ret)

# ^ 只从第一个开始

# rt = re.findall('^h...o',"hafaoffhello")
# print(rt)
# $  代表从结尾
# ret = re.findall("a..x$" , "sfalexsfsauyx")
# print(ret)

# * 重复匹配 [ 0,oo]
# rt = re.findall('ab*',"aqwerryabbbbcrrtytffdsgalllliafdsadafafda")
# print(rt)

# rt = re.findall('.*',"aqwerryabbbbcrrtytffdsgalllliafdsadafafda")
# print(rt)

# +   [1,oo]
# ret = re.findall("ca+x" , "adfcaaxfe")
# print(ret)

# ?   [0,1]
# rt = re.findall("ca?v","4234dfcavdcv")
# print(rt)


# print(re.findall("a*b" , 'aaaaaaabaab'))
# {}

# rt =re.findall("a{1,3}3" , " a3aa3aaa3aaaaa4") #{1,} 等于{1, +oo}
# print(rt)

# 结论 :  * 等于{0,正无穷}    +等于{1, +oo}  ?等于{0 ,1}


#字符集

ret = re.findall('[a-z]d' , "abcd")
print(ret)


#[] 字符集:取取消元字符的特殊功能 (\ ^ -)

# rt =re.findall("[w,,]","awd,")
# print(rt)

ret =re.findall('^iu' ,'iuweiuds')
print(ret)
# ^放在[]里,取反
ret =re.findall('[^t]' ,'iuwtt]weiuds')
print(ret)


# \
# 反斜杠后边跟元字符去除特殊功能
# 反斜杠后边跟普通字符实现特殊功能

# \d   匹配任何十进制数,相当于   [0-9]
# \D   匹配任何非数字字符;  [^0-9]
# \s   匹配任何空白字符    [\t\n\r\f\v]
# \S   匹配任何非空白字符    [^\t\n\r\f\v]
# \w   匹配任何字母数字字符   [a-zA-Z0-9]
# \W   匹配任何非字母数字字符   [^a-zA-Z0-9]
# \b   匹配一个特殊字符边界 ,也就是指单词和空格之间的位置

# ret =re.findall("\d{11}" ,"13456483518531")
# print(ret)
# ret =re.findall("\Sasd" ,"1345648asd3518531")
# print(ret)
# ret =re.findall("\w" ,"adAb 23")
# print(ret)

# ret =re.findall(r"I\b" ,"I am a LI-st")
# print(ret)


#############################
#匹配出满足条件的第一个结果
# print(re.search('sb','fjskdsbsdB'))
# ret= re.search('sb','fjskdsbsdB')
# print(ret.group())


# print(re.search("a.",'agj').group())
# print(re.search("a\+",'a+gj').group())
# print(re.search("a\.",'a.gj').group())

# print(re.findall(r'\\',"adhf\c"))
# print(re.findall(r'\bblow',"blow"))




##################################

# () |


#   |  表示 或
# print(re.search('(as)+','afasfd').group())#
# print(re.search('(as|3)+','3as').group())

#  ?p 表示起个名字    <id>表示分组
# ret =re.search('(?P<id>\d{3})/(?P<name>\w{3})',"wwwwwwew34tttt123/ooo")
#
# print(ret.group('name'))

# print(re.search('(as)+','sdjasaskf').group())
# print(re.search('(as)|3+','3sdjasas3kf').group())
#
# print(re.search('(as)|3+','3sdjasas3kf').group())
#




#正则表达式

# 1. findall() : 所有的结果都返回到一个列表中
# 2. search() : 返回匹配到第一个对象(object), 包含这匹配的信息 ; 对象可以调用group()方法 拿取返回结果
# 3. match() : 只在字符串开始匹配; 只返回一个对象,也用group 返回结果

# ret = re.match("asd","asdfjdsad")
# print(ret)
# print(ret.group())

#4. split()


# ret = re.split('[j,s]','sjksal')  # *********
# print(ret)
#
# ret = re.sub('a..x','s..d','jfefalexdsf')
# print(ret)


obj = re.compile("\.com")
ret = obj.findall("fefffs.comwf")
print(ret )



















