# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import requests

if __name__ == "__main__":
    print("requests 基本示例")

    #发送http GET请求
    resp = requests.get("https://api.github.com")

    #返回请求码
    status = resp.status_code

    #返回完整的头
    headers = resp.headers

    #返回头 content-type的值
    content_type = headers["content-type"]

    #返回内容编码类型
    code = resp.encoding

    #返回内容文本
    text = resp.text

    # 若返回结果为json格式，我们可以获取其json格式内容
    if "application/json" in content_type:
        json_data = resp.json()
    else:
        json_data = ""
    # 打印上述所有获取到的值
    print("状态码： ", status)
    print("返回头： ", headers)
    print("content-type： ", content_type)
    print("编码：", code)
    print("文本内容： ", text)
    print("json串内容: ", json_data)