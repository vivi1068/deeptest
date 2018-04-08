#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'lee'

import requests
import json
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#报错误：UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-47: ordinal not in range(128)
#需要加上上面三行

#利用requests获取网络数据并写入文件
def douban_book_search():
    try:
        url = 'https://api.douban.com/v2/book/search?'
        payload = {'q':'python', 'count':100}
        r = requests.get(url,params=payload)
        json_str = r.json()   #json_str是dict类型
        data = json.dumps(json_str)  #data是str类型
        # print json_str
        #print type(data)
        # fileName =  'd:\json.txt'
        # with open(fileName,'wb') as fd:
        #     for js in r.iter_content(1000):
        #         fd.write(js)
        # 返回json字典数据        
        return data
    except Exception,e:
        print e

#定义JSON字典转换为一个Python对象例子
class JSONObject:
    def __init__(self,d):
        self.__dict__ =  d


#  #写入文件    
# def jsonFile(fileData):
#     filename = 'd:\json.txt'
#     file = open(filename,'wb')
#     file.write(fileData)
#     file.close()

if __name__ == "__main__":
    request = douban_book_search()
    data = json.loads(request, object_hook=JSONObject)
    # count = data.count
    # start = data.start
    # total = data.total
    # books1 = data.books[0].author
    books =[]
    body = []

    #对接口返回的book的值进行遍历，提取出每个book实例的"subtitle","author","pubdata","author_intro","summary","price"
    for index in range(0,100):
        body.append(data.books[index].subtitle)
        # 因为json返回的author结果是数组，需要进行特殊处理
        author = data.books[index].author #此时直接打印，仍是列表形式[u'\u5df4\u91cc\uff08Barry.P.\uff09']
        authors = ','.join(author)  #把author里面数组的数据用逗号，连接，形成字符串 巴里（Barry.P.）
        body.append(authors)
        body.append(data.books[index].pubdate)
        body.append(data.books[index].author_intro)
        body.append(data.books[index].summary)
        body.append(data.books[index].price)
        books.append(body)
        #body插入完成后，重置为空列表
        body = []
        #print data.books[index].author[0]        

    headers=["Subtitle","Author","Pubdate","Author_intro","Summary","Price"]
    #with open('d:/books.csv', 'w+',encoding='utf-8') as fff:
    with codecs.open('d:/books.csv', 'w+','utf-8') as fff:
        fff_csv=csv.writer(fff)  
        fff_csv.writerow(headers)  
        fff_csv.writerows(books)
        # fff_csv.close() #with文件操作不需要手动关闭，会自动关闭



    # count = [1,2]
    # start = [11,22,33]
    # total = [111,222,333,444]
    # dets = []
    # dets.append(count)
    # dets.append(start)
    # dets.append(total)
    # print books1


    #定义表名
    # headers=["count","start","total","subtitle","author","pubdata","author_intro","summary","price"]
    # with open('d:/temp4.csv', 'w+') as fff:
    #     fff_csv=csv.writer(fff)  
    #     fff_csv.writerow(headers)  
    #     fff_csv.writerows(dets) 






