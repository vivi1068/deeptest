#--coding:utf-8--
#本折关于http方面的requests库 
# requests可以看做是在 client urllib基础上的更高层的实现，里面已经实现了一些底层的东西用起来更方便

import requests

if __name__=="__main__":
    #现在用requests来实现前面urllib.request实现的东西

    url_eg="https://www.cnblogs.com/flowingwind/p/8379881.html"

    #访问该网页
    response=requests.get(url_eg)

    #查看响应相关信息
    status_eg=response.status_code  #响应状态码
    print(status_eg)

    header_eg=response.headers  #响应头信息
    print(header_eg)

    #查看返回的响应内容
    body_eg=response.text   #会自动decode
    #print(body_eg)

    #响应编码
    encode_eg=response.encoding #自动使用该码解码上面的text
    print(encode_eg)
    #也可设置为其它编码 则解码text用修改后的编码
    response.encoding='gbk'
    response.encoding='utf-8'
    
    #访问的url
    url=response.url
    print(url)