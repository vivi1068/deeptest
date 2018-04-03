# __author__ ='wuwa'
# -*- coding:utf-8 -*-

"""
parse 对url进行拆分、组合
requset urllib最核心的模块，其定义了系列函数、类用于实现http/https相关协议功能
response 对相应结果做处理
robotparser 提供了一个单独的类：robotfileparser，用于处理robot.txt文件，http://www.robotstxt.org/norobots-rfc.txt
"""
import urllib.request
from urllib.parse import urlparse

if __name__ == "__main__":

    print("读取www.python.org首页的html的源码")
    openurl = "http://www.python.org"
    response = urllib.request.urlopen(openurl)
    print(response.read())

    print("\n urllib url 切割实例")
    url = "http://username:password@www.baidu.com:80/q=开源优测"

    result = urlparse(url)
    print('切割后的结果以元组方式展示')
    print(result)
    print("协议:",result.scheme)
    print("链接字符串:",result.netloc)
    print("端口号:",result.port)
    print("uri资源:",result.path)
    print("用户名:",result.username)
    print("密码:",result.password)


    print("urllib api 实例")

    # 访问百度首页
    baiduurl= "http://www.baidu.com"
    response = urllib.request.urlopen(baiduurl)

    # 打印首页的html源码
    # 获取完整的响应内容 用于断言
    html = response.read()
    # print(html)

    # 打印http header信息
    print(response.info())

    # 获取状态码 如接口测试中断言装填码
    print(response.getcode())

    # 打印本次请求的目标url
    print(response.geturl)

