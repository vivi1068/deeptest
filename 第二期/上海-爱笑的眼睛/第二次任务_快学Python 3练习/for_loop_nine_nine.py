# -*- coding:utf-8 -*-
#__author__ = u'smile eyes'

if __name__ == "__main__":
    for i in range(1,10):
        for j in range(i,10):
            print(u"%d * %d = %2d"% (i,j,i*j),end=" ")
        print("")
