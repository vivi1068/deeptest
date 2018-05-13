# -*- coding:utf-8 -*-
#__author__ = u'smile eyes'

if __name__ == "__main__":
    print(u"range for循环实例")    

    # 使用默认参数生成序列进行遍历
    for i in range(5):
        print(i, end=',')    
    
    # 换行
    print('')    
    
    # 指定范围生成序列进行遍历
    for i in range(0, 10):
        print(i, end=',')    
    
    # 换行
    print('')    
    
    # 带步长方式生成序列进行遍历
    for i in range(0, 10, 2):
        print(i, end=',')