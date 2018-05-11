# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import urllib.request
from openpyxl import Workbook


if __name__ == "__main__":
    print("爬取豆瓣网书籍数据写入excel示例")

    for start in (1, 3):
        url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
        try:
             response = urllib.request.urlopen(url)
        except:
             print("休息会儿吧")
             break

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()

    # 将string转换为dict
    ebook_dict = eval(ebook_str)

    # 构建一个Workbook对象
    # 激活第一个sheet
    wb = Workbook()
    # 写入表头
    ws = wb.active
    ws.append(["书名", "作者", "描述", "出版社", "价格"])

    # 写入书信息
    for book in  ebook_dict["books"]:
        ws.append([book["title"], ",".join(book["author"]), book["summary"], book["publisher"], book["price"]])

    # 保存
    wb.save("douban.xlsx")
