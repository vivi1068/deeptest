# __author__ ='wuwa'
# -*- coding: utf-8 -*-
"""
1、requests库为python的第三方库
2、安装requests，可以通过pip安装，也可以通过源码安装
3、requests库支持发送请求，如get、post、put等
4、获取不同类型的响应内容，如json格式、二进制格式等
5、定制请求头
6、cookie、超时、ssl认证、代理等等

"""
import requests

if __name__ =="__main__":

    # 发送请求
    url = "http://www.itwhy.org"
    r = requests.get(url)

    # 发送带有带有参数的get请求
    payload = {'key1': 'value1', 'key2': 'value2'}
    r_2 = requests.get(url=url,params=payload)
    print(r_2.url)

    # 自定义头文件,通过字典的方式
    headers = {'cookie':'123456'}
    requests.get(url=url, params=payload,headers = headers)

    # 返回码
    status_code = r.status_code

    # 头文件
    headers = r.headers

    # 头文件的content-type的值
    # content_type = r.headers["content_type"]

    # 内容的编码类型
    encoding = r.encoding

    # 文本内容
    text = r.text
    content = r.content
    raw = r.raw

    # 如果响应内容为json，则通过如下方式获取
    # json_str = r.json()

    print(status_code,headers,encoding,text,content,raw)