# __author__ = 'wuwa'
# -*- encoding :utf-8 -*-

"""
Http.client API DEMO  创建连接、请求头、请求参数、模拟发送请求、获取相应结果、处理响应内容
1.HTTPConnection
2.HTTPResponse
"""
import http
import urllib
from http.client import HTTPConnection

if __name__ == "__main__":
    print("http.client API Demo")

    print("http.client 的GET方法")

    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    #发送请求
    conn.request("GET", "/")
    # 获取响应内容
    r1 = conn.getresponse()
    # 打印装填、原因、版本
    print(r1.status, r1.reason, r1.version)
    data = r1.read()
    # print(data)

    # 按块读取响应内容
    conn.request("GET", "/")
    r1 = conn.getresponse()
    while not r1.closed:
        r_data = r1.read(200)
        if len(r_data)==0:
            break
        else:
            print("=================")
            print(r_data)
    # 请求不存在的url
    conn.request('GET','/parron.com')
    re = conn.getresponse()
    print(re.status,re.reason)
    data = re.read()
    print(data)

    # 断开连接
    conn.close()

    print("http.client HEAD DEMO")
    # 创建连接
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送请求
    conn.request('HEAD','/')
    # 获取相应结果
    re = conn.getresponse()
    # 打印状态码、原因
    print(re.status,re.reason)
    # 读取内容
    data = re.read()
    # 打印长度
    print(len(data))
    # 关闭连接
    conn.close()

    print("http.clien Post Demo")

    # 创建连接
    conn = http.client.HTTPSConnection("bugs.python.org")
    # 创建请求头
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"
    }
    # 请求参数
    params = urllib.parse.urlencode({'@number': 19999,
        '@type': 'issue',
        '@action': 'show'})
    # 发送求情
    conn.request("POST","",params,headers)
    # 获取响应内容
    re = conn.getresponse()
    # 处理响应内容
    print(re.status,re.reason)
    data = re.read()
    print(data)
    # 关闭连接
    conn.close

"""
HTTPConnection初始化定义函数，HTTPConnection(host, port=None, [timeout, ]source_address=None) ，返回httpconnection的一个实例化对象
host: 目标服务器IP或url
port: 目标服务端口(默认值 http: 80, https: 443), 可选参数 timeout： 超时参数， 可选 source_address: 用于标识链接的来源，格式为(host, port)
样例： http.client.HTTPConnection('www.python.org', 80, timeout=10, source_address=("www.baidu.com", 80)

https链接初始化 返回一个HTTPSConnection实例对象
HTTPSConnection(host, port=None, key_file=None,
    cert_file=None, [timeout, ]source_address=None,
    *, context=None, check_hostname=None)

发送http请求
HTTPConnection.request(method,
    url,
    body=None,
    headers={}, *,
    encode_chunked=False)

获取返回值，获取到的是一个HTTPResponse实例对象
HTTPConnection.getresponse()

设置调试级别,默认为0， 即不输出调试信息
用于链接出现问题时，打开调试信息，方便定位
HTTPConnection.set_debuglevel(level)

设置HTTP隧道，即运行通过代理服务器运行连接
这里的host、port指定是目标服务端的host和端口，不是代理的host和端口，代理的host和端口，应当在初始化时指定
import http.client
# 代理服务器: localhost, 端口 8080
conn = http.client.HTTPSConnection("localhost", 8080)
# www.python.org为我们的目标交互服务
conn.set_tunnel("www.python.org")
conn.request("HEAD","/index.html")
HTTPConnection.set_tunnel(host, port=None, headers=None)

# 连接到创建对象时指定的服务器。
# 默认情况下，如果客户端尚未有连接，则在发出请求时自动调用此功能。
HTTPConnection.connect()# 关闭连接HTTPConnection.close()

# 向服务器发送RFC 822样式的头。
# 它向服务器发送一条行，包括头、冒号和空格，以及第一个参数。
# 如果给出更多的参数，则会发送延续行，每个行包含一个选项卡和一个参数。
HTTPConnection.putheader(header, argument[, …])

# 向服务器发送一条空行，表示头的尾。
# 可选的messagebody参数可用于传递与该请求相关联的消息体。
HTTPConnection.endheaders(message_body=None, *,
    encode_chunked=False)

# 将数据发送到服务器。
# 在调用endheader()方法和调用getresponse()之前，
# 应该直接使用该方法。
HTTPConnection.send(data)

"""

"""
HTTPResponse
# 读取并返回响应主体
HTTPResponse.read()

# 将响应主体的下一个len(b)字节读取到缓冲区b中，
# 返回读取的字节数。
HTTPResponse.readinto(b)

# 返回头名的值，如果没有标题匹配名称，则返回默认值。
# 如果有不止一个带有name名称的头，则返回由''所连接的所有值。
# 如果“default”是除单个字符串以外的任何可迭代的，
#它的元素也会以逗号的方式返回。
HTTPResponse.getheader(name, default=None)

# 返回一个(header, value)元组的列表
HTTPResponse.getheaders()

# 返回服务器使用的HTTP协议版本。
# 10为http/1.0，11为http/1.1。
HTTPResponse.version

# 返回服务器返回的状态码# 例如200
HTTPResponse.status

# 返回服务器返回的reason描述
# 例如 OKHTTPResponse.reason

# 返回流的状态# True表示流已关闭
HTTPResponse.closed

"""

