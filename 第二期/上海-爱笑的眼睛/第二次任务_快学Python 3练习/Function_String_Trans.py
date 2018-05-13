# -*- coding:utf-8 -*-
#__author__ = u'smile eyes'

# 字符串连接函数
def str_join(str1, str2, str3):

    return str1 + str2 + str3

if __name__ == "__main__":
    print(u"字符串连接实例: ")

    str1 = u"大家好，"
    str2 = u"我的公众号是："
    str3 = u"开源优测"

    str_j = str_join(str1, str2, str3)
    print(str_j)