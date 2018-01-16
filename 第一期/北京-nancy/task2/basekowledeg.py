# -*- coding:utf-8 -*-
__author__ = 'nancy'

import keyword

if __name__ == "__main__":
    # this is note
    sum = 0  #this is note
    #sys keyword
    print(keyword.kwlist)

    #read any input
    data = input("please input any word:")
    print("your input is: %s" % data)

    #split input
    data2 = input("please input any word:")
    data_list = data2.split(' ')
    print("your input is:%s" % data_list)