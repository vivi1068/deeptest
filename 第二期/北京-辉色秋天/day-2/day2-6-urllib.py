#-*-coding:utf-8 -*-

import urllib.request
import csv
import codecs


def douban():

    print("urllib爬去豆瓣数据")
    print("关键字python")

    url = "https://api.douban.com/v2/book/search?q=python"

    response = urllib.request.urlopen(url)

    ebook_str = response.read().decode()
    ebook_dict = eval(ebook_str)

    count = ebook_dict['count']
    total = ebook_dict['total']

    with codecs.open('book.csv','w','utf-8')  as csvfile:
        spamwriter=csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])

        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"], 
                ",".join(book["author"]), 
                book["summary"], 
                book["publisher"], 
               book["price"]])


def test():
    url = "https://www.baidu.com"
    response = urllib.request.urlopen(url)
    print(response.status)

    print(response.reason)

    print(response.headers)

    print(response.read().decode("utf-8"))


if __name__ == "__main__":
    test()
