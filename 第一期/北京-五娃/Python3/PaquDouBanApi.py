# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
豆瓣网API网址：https://developers.douban.com/wiki/?title=guide
"""
import urllib.request
import csv
import codecs

url = "https://api.douban.com/v2/book/search?q=python"
response = urllib.request.urlopen(url)
# 将相应结果转为字典
ebook_str = response.read().decode()
ebook_dict = eval(ebook_str)
print(ebook_dict)
count = ebook_dict["count"]
total = ebook_dict["total"]

with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
    for book in ebook_dict["books"]:
        spamwriter.writerow([book["title"],
                             ",".join(book["author"]),
                             book["summary"],
                             book["publisher"],
                             book["price"]]
                            )
    """
    将页码按照range(1, int(total / count) + 1)进行变更
           for start in range(1, int(total / count) + 1):
               url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
               try:
                   response = urllib.request.urlopen(url)
               except:
                   print("别老爬别人的数据，要爬也别太快，会被封IP的")
                   break


               # 将bytes数据流解码成string
               ebook_str = response.read().decode()

               # 将string转换成dict
               ebook_dict = eval(ebook_str)

               # 输出书籍信息
               for book in ebook_dict["books"]:
                   spamwriter.writerow([book["title"],
                   ",".join(book["author"]),
                   book["summary"],
                   book["publisher"],
                   book["price"]])
           """
    print("总计搜索了 %d 本书的信息" % total)
