#-*- coding:utf-8 -*-

if __name__ == "__main__":
    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"
    print(u"从左往右找yo")
    print("find结果是"+ str(source_str.find('yo')))
    print("index结果是"+ str(source_str.index('yo')))

    print("从有往左找yo")
    print("rfind 结果是"+str(source_str.rfind("yo")))
    print("rindex 结果是"+str(source_str.rindex("yo")))

    print("替换所有 yo")
    print(source_str.replace("yo", "xx"))

    print("替换2次 yo")
    print(source_str.replace("yo", 'rr', 2))
    
