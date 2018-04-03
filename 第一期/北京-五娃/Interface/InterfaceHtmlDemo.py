# __author__ ='wuwa'
# -*- coding: utf-8 -*-
from html.parser import HTMLParser

import requests

"""
1、初始化操作
2、执行handle—starttag
3、执行handle—data
4、执行handle—endtag
5、重复2、3、4 步骤
"""


class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        """
        初始化操作
        """
        HTMLParser.__init__(self)
        # 状态标记
        self.is_a = False

    def handle_starttag(self, tag, attrs):
        """
        处理开始为tag的标签
        :param tag:
        :param attrs:
        :return:
        """
        if tag == 'a':
            # 如果tag 是a标签，则将is_a的状态置为True，同时提取a标签的href属性值
            self.is_a = True
            for name, value in attrs:
                if name == "href":
                    self.data_key = value

    def handle_data(self, data):
        """
        处理标签之间的数据
        :param data:
        :return:
        """
        if self.is_a and self.lasttag == "a":
            # 将标签的href属性值作为key，文本作为data的值
            self.data.append({self.data_key: data})

    def handle_endtag(self, tag):
        """
        处理结束为tag的标签
        :param tag:
        :return:
        """
        if self.is_a and self.lasttag == "a":
            # 如过lasttag为tag，则状态置为False
            self.is_a = False

    def get_data(self):
        """
        获取目标数据
        :return:
        """
        return self.data


if __name__ == "__main__":
    print("访问博客网，获取首页的html源码")
    url = "https://www.cnblogs.com/"
    data = requests.get(url)
    # print(data.text)
    blogs = BlogHTMLParser()
    blogs.feed(data.text)
    links = blogs.get_data()
    # print(links)
    for link in links:
        print(link)
