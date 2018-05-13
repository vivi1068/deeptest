# -*- coding:utf-8 -*-
#__author__ = u'smile eyes'

if __name__ == "__main__":
    #  for字典遍历
    dict_1 = {u"开源优测": u"DeepTest", u"python": u"快学Python3"}

    print(u"遍历字典方式一，并打印出来： ")    
    for (key, value) in dict_1.items():
        print("%s : %s " % (key, value))

    print("\n-----------------------------")

    print(u"遍历字典方式二，并打印出来： ")
    for key in dict_1:
        print("%s : %s " % (key, dict_1[key]))