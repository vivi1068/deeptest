#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 9:05
# @Author  : yulu
# @File    : http_study
import urllib.request
import csv
import codecs

if __name__ == "__main__":
    print("搜索关键字：python")

    url = "https://api.douban.com/v2/book/search?q=python"
    respone = urllib.request.urlopen(url)

    # 将bytes数据解码成string
    ebook_str = respone.read().decode()
    print(ebook_str)

    # 将string转为dict
    ebook_dict = eval(ebook_str)
    print(ebook_dict)
    count = ebook_dict["count"]
    tatal = ebook_dict["total"]
    print(count,tatal)
    with codecs.open('books.csv','w','utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名","作者","描述","出版社","价格"])
        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"],
                ",".join(book["author"]),
                         book["summary"],
                         book["publisher"],
                         book["price"]])
