#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 12:59
# @Author  : gonghuihui
# @File    : parse_html

# 对贵公司最复杂的页面进行数据提取分类。
# 形成一个html解析通用类
from html.parser import HTMLParser
import http.client

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_div = False

    def handle_starttag(self, tag, attrs):
        # 处理开始为 a的标签
        if tag == "div":
            self.is_div = True
            for name, value in attrs:
                if name == "class":
                    self.data_key = value

    def handle_data(self, data):
        # 处理结束为 a 的标签
        if self.is_div and self.lasttag == "div":
            # 将a标签的href属性值做为key, a的文本做为data构建字典
            self.data.append({self.data_key: data})

    def handle_endtag(self, tag):
        # 处理a的结束标签
        if self.is_div and self.lasttag == "div":
            self.is_div = False

    def get_data(self):
        # 返回所有从a中提取到的目标数据
        return self.data

if __name__ == "__main__":
    print("Python HTML解析实例")
    # 构建链接
    url = "www.dianjia.io"
    # conn = http.client.HTTPSConnection("www.cnblogs.com")
    conn = http.client.HTTPSConnection(url)

    # 获取html源码
    conn.request("GET", "/")
    r1 = conn.getresponse()
    data = r1.read().decode(encoding="utf-8")
    # print("-------------",data)

    # 解析博客园首页html源码， 提取所有a的href和文本数据
    blogHtmlParser = BlogHTMLParser()
    blogHtmlParser.feed(data)
    links = blogHtmlParser.get_data()

    print(links)