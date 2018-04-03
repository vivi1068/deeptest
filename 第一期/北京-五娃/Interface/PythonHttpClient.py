# __author__ ='wuwa'
# -*- coding : utf-8 -*-

"""
1. Http/1.1 client 的工作流程

(null)
    |
    | HTTPConnection() 建立HTTP链接
    v
Idle
    |
    | putrequest() 准备请求内容
    v
Request-started
    |
    | ( putheader() )*  endheaders() 准备请求头
    v
Request-sent 发送请求
    |\_____________________________
    |                              | getresponse() raises 获取服务端响应
    | response = getresponse()     | ConnectionError
    v                              v
Unread-response                Idle
[Response-headers-read] 响应头读取
    |\____________________
    |                     |
    | response.read()     | putrequest() 自己往下看吧
    v                     v
Idle                  Req-started-unread-response
                    ______/|
                /        |
response.read() |        | ( putheader() )*  endheaders()
                v        v
    Request-started    Req-sent-unread-response
                        |
                        | response.read()
                        v
                        Request-sent
2. 支持HTTP/1.1的协议
3. HTTPS的支持需要安装SSL

流程理解-创建连接-请求头信息-发送请求-获取服务端响应-处理响应内容

"""