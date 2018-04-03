# -*- coding:utf-8 -*-
__author__ = "Lakisha"

import unittest
import http.client
import logging

## 日志管理类
Logging_Format = '%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s'

class LQLogging:
    def __init__(self,
                 level=logging.DEBUG,
                 format=Logging_Format,
                 datefmt='%a, %d %b %Y %H:%M:%S',
                 filename='LQ.log',
                 filemode='w'
                 ):
        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode = filemode

        # 初始化日志同时输出到console和日志文件
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode
                            )

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，
        # 并将其添加到当前的日志处理对象
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logger = logging.getLogger("LQ")
        logger.addHandler(console)

        self.log = logger

    def output(self,msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            self.log.debug(msg)
        elif level == logging.INFO:
            # 一般的信息
            self.log.info(msg)
        elif level == logging.WARNING:
            # 警告信息
            self.log.warning(msg)
        elif level == logging.ERROR:
            # 错误信息
            self.log.error(msg)
        else:
            # 尼玛
            self.log.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.setLevel(level)


## http client封装
class LQHTTP:
    def __init__(self, protocol, host, port=80,
                 key_file=None,
                 cert_file=None,
                 timeout=30,
                 log_level=logging.INFO
                 ):
        # self.protocol = protocol
        self.host = host
        self.port = port
        self.cert_file = cert_file
        self.key_file = key_file
        self.timeout = timeout

        self.response = None
        self.data = None
        self.status = None
        self.reason = None
        self.headers = None

        self.log_level = log_level
        self.log = LQLogging(level=self.log_level)
        self.log.output("初始化http连接到: %s:%d" % (host, port))

        self.http = None
        if protocol == "http":
            self.http = http.client.HTTPConnection(host=self.host, port=self.port, timeout=self.timeout)
        elif protocol =="https":
            self.http = http.client.HTTPSConnection(host=self.host, port=self.port, timeout=self.timeout,
                                                    key_file=self.key_file, cert_file=self.cert_file
                                                   )
        else:
            print("不支持的协议类型", protocol)
            exit()

    #返回response对象
    def request(self, method, url, body=None, headers={}):
        self.http.request(method=method, url=url, body=body, headers=headers)
        self.response = self.http.getresponse()
        self.data = self.response.read()
        self.status = self.response.status
        self.reason = self.response.reason
        self.headers = self.response.getheaders()

        self.log.output("------" * 10, self.log_level)
        self.log.output("\nrequest")
        self.log.output("\nurl: %s \nmethod: %s \nheaders: %s \ndata: %s" %
                        (url, method, headers, body), self.log_level)
        self.log.output("\nresponse")
        self.log.output("\nstatus: %s \nreason: %s \nheaders: %s \ndata: %s" %
                        (self.status, self.reason, self.headers, self.data), self.log_level)
        return self.response

    def close(self):
        if self.http:
            self.http.close()

    def get_data(self):
        return self.data

    # 返回指定响应头
    def get_header(self, name):
        for header in self.headers:
            if header[0] == name:
                return header[1]
        return None

    # 返回完整的响应头
    def headers(self):
        return self.headers

    # 返回状态码及文本说明
    def get_status_reason(self):
        return (self.status, self.reason)

#Page基类
class Page:
    def __init__(self, protocol, host, port=80, key_file=None,
                 cert_file=None, timeout=30, log_level=logging.INFO):

        self.http = LQHTTP(protocol=protocol, host=host, port=port, key_file=key_file,
                           cert_file=cert_file, timeout=timeout, log_level=log_level)

    def request(self, method, url, body=None, headers={}):
        self.http.request(method=method, url=url, body=None, headers={})

    def close(self):
        if self.http:
            self.http.close()


# 豆瓣API
class BookSearchPage(Page):
    def __init__(self, protocol, host, port=80,
                 key_file=None,  # ssl
                 cert_file=None,  # ssl
                 timeout=30,
                 log_level=logging.INFO):
        Page.__init__(self, protocol=protocol,
                      host=host,
                      port=port,
                      key_file=key_file,
                      cert_file=cert_file,
                      timeout=timeout,
                      log_level=log_level)
        # 查询python相关的书籍

    def search_python_book(self, method, url,
                           body=None, headers={}):
        self.request(method=method, url=url, body=body,
                     headers=headers)
        return self.http.get_data()


# 测试用例
class TestSearchBookPage(unittest.TestCase):
    def setUp(self):
        self.book_search_page = BookSearchPage(protocol="https",
                                               host="api.douban.com", port=443)

    def test_search_python_book(self):
        # 查找python相关的书籍即q=python，只找两本即count=2
        books = self.book_search_page.search_python_book(method="GET",
                                                         url="/v2/book/search?q=python&count=2")

        # 获取并断言下http status及reason
        status, reason = self.book_search_page.http.get_status_reason()
        self.assertEqual(status, 200)
        self.assertEqual(reason, "OK")

        # 获取并断言下http header 例如断言下返回的Content-Type是不是application/json; charset=utf-8
        content_type = self.book_search_page.http.get_header("Content-Type")
        self.assertEqual(content_type, "application/json; charset=utf-8")

        # 看一下返回的数据类型
        print("/v2/book/search?q=python&count=2返回的数据类型为： ", type(books))

        # 断言下返回类型
        self.assertIsInstance(books, bytes)

        # 强制将bytes类转成成dcit类型
        # 这里运行时 可能会出现一些警告信息，不用理会
        books_dict = eval(str(books, encoding="utf-8"))

        # 断言下count计数，应该为2, 因为我们只查找2本
        self.assertEqual(books_dict["count"], 2)

    def tearDown(self):
        self.book_search_page.close()

if __name__ == "__main__":
    print("http.client Restful API测试实例")
    unittest.main()