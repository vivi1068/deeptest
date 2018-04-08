# __author__ ='wuwa'
# -*- coding: utf-8 -*-
import requests

if __name__ == "__main__":
    # 待提交数据
    payload = {'key1': 'value1', 'key2': 'value2'}

    # 发送post请求
    r = requests.post("http://httpbin.org/post", data=payload)
    # print(r.text)

    # 多个元素使用同一个key
    payload = (('key1', 'value1'), ('key1', 'value2'))
    r = requests.post('http://httpbin.org/post', data=payload)
    print(r.text)

    # 待提交数据为json类型
    url = 'http://httpbin.org/post'
    json_data = {'title': 'python', 'type': '2'}
    headers = {'cookies': 'hello'}
    r = requests.post(url=url, json=json_data, headers=headers)
    print('=============================')
    print(r.text)

    # 数据流文件的请求为multipart/form-data，通过 requests-toolbelt 包实现
