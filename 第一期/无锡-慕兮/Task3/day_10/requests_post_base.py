# -*- coding:utf-8 -*-
__author__ = 'Lakisha'
import requests

#headers 自定义
'''
if __name__ == "__main__":
    print("开源优测 - requests自定义请求头基本示例")
    url = "http://www.baidu.com"
    # 定义自定义请求头数据
    headers = {"user-agent": "www.testingunion.com","custom-head": "DeepTest"}
    # 发送带自定义头的请求
    r = requests.get(url, headers=headers)
'''

if __name__ == "__main__":
    print("requests post示例")
    #目标url
    url = "http://httpbin.org/post"
    #请求头headers
    headers = {"custom-header": "mypost"}
    # 要post的数据
    data = {"data_1": "deeptest", "data_2": "testingunion.com"}
    # 发送post请求
    r = requests.post(url, data=data, headers=headers)
    # 输出结果
    print(r.text)
