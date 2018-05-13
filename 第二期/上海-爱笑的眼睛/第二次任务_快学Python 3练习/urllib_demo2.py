# -*- coding:utf-8 -*-
#__author__ = 'smile eyes'

import urllib.request

if __name__ == "__main__":    
    print("urllib基本实例")

    url = "http://www.baidu.com"

    # 访问下百度
    response = urllib.request.urlopen(url)    

    # 打印下状态码
    print(response.status)    
    
    # 打印下状态码对应的可读性文字说明，例如在http协议里，200 对应 OK
    print(response.reason)    
    
    # 打印下请求返回的header
    print(response.headers)    
    
    # 打印下请求返回的数据
    print(response.read().decode("utf-8"))