# coding=utf-8

'''

概述

urllib是python最基础、最核心的HTTP协议支持库，诸多第三方库都依赖urllib，所以urllib是必须掌握的HTTP库。

掌握了urllib有利于：

深入理解http协议
可以更好的学习和掌握第三方http库
快速的开展基于http的接口测试
快速进入爬虫学习之路
'''

'''
urllib.request
用于构建http请求

urllib.response
用于处理http响应值的类

urllib.parse 用于url处理

urllib.error
用于错误处理

urllib.robotparser
用于处理robot.txt文件
'''
import urllib.request, urllib.response, urllib.parse, urllib.error, urllib.robotparser
import csv
import urllib.request
import codecs

if __name__ == "__main__":
    print("urllib爬取豆瓣网数据示例")
    print("搜索下关键字： Python")

    url = "https://api.douban.com/v2/book/search?q=python"
    response = urllib.request.urlopen(url)

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()

    # 将string转换成dict
    ebook_dict = eval(ebook_str)

    # print(ebook_dict)
    # print(type(ebook_dict))
    count = ebook_dict["count"]
    total = ebook_dict["total"]

    with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
        # 写书信息
        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"],
                                 ",".join(book["author"]),
                                 book["summary"],
                                 book["publisher"],
                                 book["price"]])

        # 从第2页开始，获取其他书籍信息
        # 这段代码采集了大量数据，容易被封IP，所以注释了
        """
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
'''
请勿使用上述代码持续爬取数据

请勿使用上述代码持续爬取数据

请勿使用上述代码持续爬取数据

对于其他的接口，这里就不再演示。

基本功能实例

下面我们演示下urllib基本功能实例，例如如何获取返回码等等基本信息。
'''
# -*- coding:utf-8 -*-



import urllib.request

if __name__ == "__main__":
    print("urllib基本实例")

    url = "http://www.baidu.com"

    # 访问下百度
    response = urllib.request.urlopen(url)

    # 打印下状态码
    print(response.status)

    # 打印下状态码对应的可读性文字说明，例如在http协议里，200 对应 OK
    print(response.reason)

    # 打印下请求返回的header
    print(response.headers)

    # 打印下请求返回的数据
    print(response.read().decode("utf-8"))
