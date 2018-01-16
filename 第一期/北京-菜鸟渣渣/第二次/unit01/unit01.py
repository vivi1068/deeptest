# -*- coding:utf-8 -*-
__author__ = 'Young'

import http.client, urllib.parse

OP_ASSIGN = 'OP_ASSIGN'
OP_DELETE = 'OP_DELETE'
OP_APPLY = 'OP_APPLY'

SC_LOCAL = 1
SC_GLOBAL_IMPLICIT = 2
SC_GLOBAL_EXPLICIT = 3
SC_FREE = 4
SC_CELL = 5
SC_UNKNOWN = 6

CO_OPTIMIZED = 0x0001
CO_NEWLOCALS = 0x0002
CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008
CO_NESTED = 0x0010
CO_GENERATOR = 0x0020
CO_GENERATOR_ALLOWED = 0
CO_FUTURE_DIVISION = 0x2000
CO_FUTURE_ABSIMPORT = 0x4000
CO_FUTURE_WITH_STATEMENT = 0x8000
CO_FUTURE_PRINT_FUNCTION = 0x10000

if __name__ == "__main__":
    print("http.client基本示例")

    print("http.client GET方法示例")
    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送GET请求
    conn.request("GET", "/")
    # 获取响应
    r1 = conn.getresponse()
    # 打印状态码、对应说明、协议版本
    print(r1.status, r1.reason, r1.version)
    # 读取整个响应内容
    data1 = r1.read()

    # 下面代码演示如何分chunck读取内容
    conn.request("GET", "/")
    r1 = conn.getresponse()
    ''''
    r2 = conn.request(self, host, handler, request_body, verbose=False):
        parts = (self._scheme, host, handler, None, None, None)
        url = urllib_parse.urlunparse(part)
    '''
    while not r1.closed:
        # 每次读取200bytes
        r1_data = r1.read(200)
        if len(r1_data) == 0:
            break
        print(r1_data)

    # 请求不存在的url
    conn.request("GET", "/parrot.spam")
    r2 = conn.getresponse()
    print(r2.status, r2.reason)
    data2 = r2.read()
    # 断开连接
    conn.close()

    print("http.client HEAD方法")
    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("HEAD", "/")
    res = conn.getresponse()
    print(res.status, res.reason)

    data = res.read()
    print(len(data))
    conn.close()

    print("http.client POST方法")
    # 请注意这里设置http headers的方法
    params = urllib.parse.urlencode({'@number': 19999,
                                     '@type': 'issue',
                                     '@action': 'show'})
    # http头参数
    headers = {"Content-type":
                   "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = http.client.HTTPConnection("bugs.python.org")
    # 把请求的data和头参数一起传入
    conn.request("POST", "", params, headers)
    # 获取响应对象
    response = conn.getresponse()
    # 打印响应状态
    print(response.status, response.reason)
    # 读取响应内容
    data = response.read()
    print(data)
    # 关闭连接
    conn.close()

'''


'''
"""Force name to be global in scope.

        Some child of the current node had a free reference to name.
        When the child was processed, it was labelled a free
        variable.  Now that all its enclosing scope have been
        processed, the name is known to be a global or builtin.  So
        walk back down the child chain and set the name to be global
        rather than free.

        Be careful to stop if a child does not think the name is
        free.
"""
mygenerator = (x * x for x in range(3))
print mygenerator
for i in mygenerator:
    print(i)
print "----------------"


def createGenerator():
    mylist = range(10)
    for i in mylist:
        yield i * i


generator = createGenerator()
for s in generator:
    print s



