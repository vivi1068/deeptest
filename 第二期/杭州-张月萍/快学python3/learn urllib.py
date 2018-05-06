# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import urllib.request
import csv
import codecs


if __name__ == "__main__":
    print('urllib爬取豆瓣网数据示例')
    print('搜索关键字：Python')

    # 豆瓣网API网址：https://developers.douban.com/wiki/?title=guide
    url = 'https://api.douban.com/v2/book/search?q=python'
    response = urllib.request.urlopen(url)

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()
    #print(ebook_str)

    # 将string转换为dict
    ebook_dict = eval(ebook_str)
    #print(ebook_dict)

    count = ebook_dict["count"]
    total = ebook_dict["total"]

    with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
        # 书写信息
        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"], ",".join(book["author"]), book["summary"], book["publisher"], book["price"]])
            # 从第2页开始，获取其他书籍信息
            # 爬取全部数据,请准备代理IP数据，不然容易被封
            # for start in range(1, int(total/count)+1)
            for start in (1, 3):
                url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
                try:
                    response = urllib.request.urlopen(url)
                except:
                    print("休息会儿吧")
                    break

                # 将bytes数据流解码成string
                ebook_str = response.read().decode()

                # 将string转换成dict
                ebook_dict = eval(ebook_str)

                # 输出书籍信息
                for book in ebook_dict["books"]:
                    spamwriter.writerow([book["title"], ",".join(book["author"]), book["summary"], book["publisher"], book["price"]])
                print(book)
