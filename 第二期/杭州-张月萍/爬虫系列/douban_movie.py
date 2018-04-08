# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import requests
import pandas
from bs4 import BeautifulSoup

url = "https://movie.douban.com/subject/26861685/comments"
r = requests.get(url).text
#print(r)
soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('p', class_='')
comments = []
for item in pattern:
    print(item.string)
    comments.append(item.string)
df = pandas.DataFrame(comments)
# 未指定路径时，csv文件同PY文件一个目录
#df.to_csv('comments.csv')
# 指定文件路径，并自动转码
df.to_csv('C:/Users/Carina/Desktop/comments.csv', encoding='utf_8_sig')

