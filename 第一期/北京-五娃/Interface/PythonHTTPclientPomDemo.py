# __author__:'wuwa'
# -*- encoding:utf-8 -*-

"""
豆瓣图书相关开放的API请参考：https://developers.douban.com/wiki/?title=book_v2
需要了解以下知识和技术：

http.client常用API
testunit
logging
PO模式（核心分离测试对象和测试数据）
"""

# http管理类
import http.client
import logging
import unittest

# 日志管理类
LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'


class LYMLogging:
    def __init__(self, level=logging.DEBUG, format=LOGGING_FORMAT, datefmt='%a, %d %b %Y %H:%M:%S', filename='LYM.log',
                 filemode='w'):

        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode = filemode
        # 初始化日志同时输出到console和日志文件
        logging.basicConfig(level=self.level, format=self.format, datefmt=self.datefmt, filename=self.filename,
                            filemode=self.filemode)

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，
        # 并将其添加到当前的日志处理对象
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('LYMHTTPLogger').addHandler(console)
        self.log = logging.getLogger("LYMHTTPLogger")

        # 日志输出

    def output(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
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
        self.log.set_level(level)


class LYMHttp:
    def __init__(self, protocol, host, port=80, key_file=None, cert_file=None, timeout=30, log_level=logging.INFO):
        """
        connection 初始化
        :param protocol:
        :param host:
        :param port:
        :param key_file:
        :param cert_file:
        :param timeout:
        :param log_level:
        """
        self.log_level = log_level
        self.log = LYMLogging(level=log_level)
        self.log.output("初始化http连接到: %s:%d" % (host, port))

        self.host = host
        self.port = port
        self.key_file = key_file
        self.cert_file = cert_file
        self.timeout = timeout
        self.response = None
        self.data = None
        self.status = None
        self.reason = None
        self.headers = None
        self.http = None

        if protocol == "http" or protocol == "HTTP":
            self.http = http.client.HTTPConnection(host=self.host, port=self.port, timeout=self.timeout)
        elif protocol == "https" or protocol == "HTTPS":
            self.http = http.client.HTTPSConnection(host=self.host, port=self.port, key_file=self.key_file,
                                                    cert_file=self.cert_file, timeout=self.timeout)
        else:
            print("不支持的协议类型:", protocol)
            exit()

    def request(self, method, url, body=None, headers={}):
        """
        返回response的响应对象
        :param method:
        :param url:
        :param body:
        :param headers:
        :return:
        """

        self.http.request(method=method, url=url, body=body, headers=headers)

        self.response = self.http.getresponse()

        self.data = self.response.read()
        self.status = self.response.status
        self.reason = self.response.reason
        self.headers = self.response.getheaders
        self.log.output("------" * 10, self.log_level)
        self.log.output("\n send requests")
        self.log.output("\n url: %s \n method: %s \n headers: %s \n data: %s" % (url, method, headers, body),
                        self.log_level)
        self.log.output("\nresponse")
        self.log.output("\n status: %s \n reason: %s \n headers: %s \n data: %s" % (
        self.status, self.reason, self.headers, self.data), self.log_level)
        return self.response

    def close(self):
        """
        关闭连接
        :return:
        """
        if self.http:
            self.http.close()

    def get_data(self):
        """
        获取响应内容
        :return:
        """
        return self.data

    def headers(self):
        """
        返回完整的响应头
        :return:
        """
        return self.headers

    def get_status_reason(self):
        """
        返回状态码及文本说明
        :return:
        """
        return (self.status, self.reason)


class Page:
    """
    page基类，所有的page models 都需要继承该类
    """

    def __init__(self, protocol, host, port=80, key_file=None, cert_file=None, timeout=30, log_level=logging.INFO):
        self.http = LYMHttp(protocol=protocol, host=host, port=port, key_file=key_file, cert_file=cert_file,
                            log_level=log_level)

    def request(self, method, url, body=None, headers={}):
        self.http.request(method=method, url=url, body=body, headers={})

    def close(self):
        if self.http:
            self.http.close()


class BookSearchPage(Page):
    """
    豆瓣api
    """

    def __init__(self, protocol, host, port=80, key_file=None, cert_file=None, timeout=30, log_level=logging.INFO):
        Page.__init__(self, protocol=protocol, host=host, port=port, key_file=key_file, cert_file=cert_file,
                      timeout=timeout, log_level=log_level)

    def search_python_book(self, method, url, body=None, headers={}):
        """
        查询python相关的书籍
        :param method:
        :param url:
        :param body:
        :param headers:
        :return:
        """

        self.request(method=method, url=url, body=None, headers={})
        return self.http.get_data()


class TestSearchBookPage(unittest.TestCase):
    def setUp(self):
        self.book_serach_page = BookSearchPage(protocol="https", host="api.douban.com", port=443)

    def tearDown(self):
        self.book_serach_page.close()

    def test_search_python_book(self):
        """
        查找python相关的书籍即q=python，只找两本即count=2
        :return:
        """
        books = self.book_serach_page.search_python_book(method="GET", url="/v2/book/search?q=python&count=2")

        # 获取响应内容状态码以及文本说明
        status, reason = self.book_serach_page.http.get_status_reason()
        self.assertEqual(status, 200)
        self.assertEqual(reason, "OK")

        print("/v2/book/search?q=python&count=2返回的数据类型为： ", type(books))

        # 断言下返回类型
        self.assertIsInstance(books, bytes)

        # 强制将bytes类型转换为dict类型
        book_dicts = eval(str(books, encoding="utf-8"))

        self.assertEqual(book_dicts["count"], 2)


if __name__ == "__main__":
    unittest.main()
