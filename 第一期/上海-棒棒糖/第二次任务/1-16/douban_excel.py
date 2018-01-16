__author__='棒棒糖'
import urllib.request
from openpyxl import Workbook
if __name__=='__main__':
    print('爬取豆瓣网书籍数据写入excel示例')
    url='https://api.douban.com/v2/book/search?q=python'
    response=urllib.request.urlopen(url)
    ebook_str=response.read().decode()
    ebook_dict=eval(ebook_str)
    #构建一个Workbook对象
    wb=Workbook()
    ws=wb.active
    ws.append(["书名", "作者", "描述", "出版社", "价格"])
    #写入信息
    for book in  ebook_dict['books']:
        ws.append([book['title'],','.join(book['author']),book['summary'],book['publisher'],book['price']])
    #保存
    wb.save('ebook.xlsx')