#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-27 下午9:58
# @Author  : gonghuihui
# @File    : http_client_demo.py
import http.client, urllib.parse

if __name__ == "__main__":
    print("http.client 基本实例")
    print("http.client GET方法的基本实例")
    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送get请求
    conn.request("GET", "/")
    # 获取响应
    r1 = conn.getresponse()
    # 打印状态码、对应说明、协议版本
    print("-1--" * 20)
    print(r1.status, r1.reason, r1.version)
    # 读取整个响应内容
    data1 = r1.read()
    print("-2--" * 20)
    # print(data1)
    # 分 chunck 读取
    conn.request("GET", "/")
    r1 = conn.getresponse()
    while not r1.closed:
        r1_data = r1.read(200)
        if len(r1_data) == 0:
            break
        # print("-3--" * 20)
        # print(r1_data)

    # 请求不存在的url
    conn.request("GET", "/parrot.spam")
    r2 = conn.getresponse()
    print(r2.status, r2.reason)
    data2 = r2.read()
    conn.close()

    print("http.client HEAD方法")
    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("HEAD", "/")
    res = conn.getresponse()
    print(res.status, res.reason)

    data = res.read()
    print("-4--" * 20)
    print(len(data))
    conn.close()

    print("http.client POST方法")

    params = urllib.parse.urlencode({'@number': 19999,
                                     '@type': 'essue',
                                     '@action': 'show'})
    headers = {"Content-type":
               "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print("-5--" * 20)
    print(data)