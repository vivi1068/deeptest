# __author__ ='wuwa'
# -*- coding:utf-8 -*-
import urllib.request
from html.parser import HTMLParser

"""
1、通过“标签”查找到对应内容，并通过标志位作为标记是否要找，为True时为找到该标签
2、处理内容获取想要的数据
3、通过标签判断是否为engtag，若是，则将标志位的值修改为False
4、通过freed方式获取数据
5、展示最终结果
"""

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.is_a = True
            for name, value in attrs:
                self.data_key = value

    def handle_data(self, data):
        if self.is_a and self.lasttag == "a":
            self.data.append({self.data_key: data})

    def handle_endtag(self, tag):
        if self.is_a and self.lasttag == "a":
            self.is_a = False

    def get_data(self):
        return self.data


if __name__ == "__main__":
    # 请求博客园官网
    url = "https://www.cnblogs.com/"

    response = urllib.request.urlopen(url)

    # 获取首页的代码
    data = response.read().decode(encoding="utf-8")

    blogHTMLparser = BlogHTMLParser()
    blogHTMLparser.feed(data)
    links = blogHTMLparser.get_data()
    print(links)
