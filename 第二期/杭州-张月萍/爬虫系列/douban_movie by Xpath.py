# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import requests
from lxml import etree


url = "https://movie.douban.com/subject/26861685/comments"
r = requests.get(url).text
# print(r)

s = etree.HTML(r)

# 浏览器复制
print(s.xpath('//*[@id="comments"]/div[10]/div[2]/p/text()'))   # 某一条评论
print("评论用户:" + str(s.xpath('//*[@id="comments"]/div[2]/div[2]/h3/span[2]/a/text()')))   # 评论用户

# 手写xpath
i = 0
comments = s.xpath('//*[@id="comments"]/div/div[@class="comment"]/p')
print(len(comments))
# while i <= len(comments):
#     print('第', i+1, '个短评：', s.xpath('//div[@class="comment"]/p/text()')[i])
#     i += 1

for i in range(len(comments)):
    #print(i)
    print('第', i+1, '个短评：', s.xpath('//div[@class="comment"]/p/text()')[i])
    i += 1


