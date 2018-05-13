# -*- coding:utf-8 -*-
#__author__ = 'smile eyes'

import sys

if __name__ == "__main__":
    seq_tuple = (34, 32, 33, 34, 35)    
    
    # 创建迭代器
    seq_it = iter(seq_tuple)
    
    # 访问打印第一个元素
    print("第一个元素：%s" % next(seq_it))    
    
    # 访问打印第二个元素
    print("第二个元素：%s" % next(seq_it))    
    
    # 访问打印第三个元素
    print("第三个元素：%s" % next(seq_it))    
    
    # 使用for循环来遍历迭代器对象
    print("\nfor循环遍历迭代器对象： ")
    for_it = iter(seq_tuple)
    for x in for_it:
        print(x, end=' ')    
        
    # 使用while结合next遍历迭代器对象
    print("\n\nwhile & next遍历迭代器对象： ")
    while_it = iter(seq_tuple)    
    while True:
        try:            
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()