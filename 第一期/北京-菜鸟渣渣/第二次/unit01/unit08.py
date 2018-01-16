# coding=utf-8
__author__ = 'Young'
import urllib2
from   io import StringIO
import   HTMLParser
# from html.parser import HTMLParser

# from html.entities import name2codepoint
class MyHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "li":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "data-cityid":
                        self.links.append(value)


if __name__ == "__main__":
    html_code = """ <ul class="open-context"><li data-cityid="76" data-cityname="广州" class="open-context-item">广州</li><li data-cityid="77" data-cityname="深圳" class="open-context-item active">深圳</li><li data-cityid="52" data-cityname="北京" class="open-context-item">北京</li><li data-cityid="321" data-cityname="上海" class="open-context-item">上海</li><li data-cityid="180" data-cityname="武汉" class="open-context-item">武汉</li><li data-cityid="192" data-cityname="咸宁" class="open-context-item">咸宁</li><li data-cityid="220" data-cityname="南京" class="open-context-item">南京</li><li data-cityid="221" data-cityname="苏州" class="open-context-item">苏州</li><li data-cityid="222" data-cityname="无锡" class="open-context-item">无锡</li><li data-cityid="235" data-cityname="赣州" class="open-context-item">赣州</li><li data-cityid="244" data-cityname="沈阳" class="open-context-item">沈阳</li><li data-cityid="245" data-cityname="大连" class="open-context-item">大连</li><li data-cityid="284" data-cityname="青岛" class="open-context-item">青岛</li><li data-cityid="322" data-cityname="成都" class="open-context-item">成都</li><li data-cityid="343" data-cityname="天津" class="open-context-item">天津</li><li data-cityid="144" data-cityname="廊坊" class="open-context-item">廊坊</li><li data-cityid="111" data-cityname="贵阳" class="open-context-item">贵阳</li><li data-cityid="53" data-cityname="福州" class="open-context-item">福州</li><li data-cityid="60" data-cityname="厦门" class="open-context-item">厦门</li><li data-cityid="78" data-cityname="潮州" class="open-context-item">潮州</li><li data-cityid="79" data-cityname="东莞" class="open-context-item">东莞</li><li data-cityid="80" data-cityname="佛山" class="open-context-item">佛山</li><li data-cityid="82" data-cityname="惠州" class="open-context-item">惠州</li><li data-cityid="83" data-cityname="江门" class="open-context-item">江门</li><li data-cityid="86" data-cityname="梅州" class="open-context-item">梅州</li><li data-cityid="92" data-cityname="云浮" class="open-context-item">云浮</li><li data-cityid="95" data-cityname="中山" class="open-context-item">中山</li><li data-cityid="96" data-cityname="珠海" class="open-context-item">珠海</li><li data-cityid="97" data-cityname="南宁" class="open-context-item">南宁</li><li data-cityid="383" data-cityname="杭州" class="open-context-item">杭州</li></ul>"""
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    print(hp.links)


# f = StringIO('Hello!\nHi!\nGoodbye!')

# while True:
# s = f.readline()
#     if s == '':
#         break
#     print s.strip()

url_save = "http://www.baidu.com"

try:
    s_save = urllib2.urlopen(url_save).read()
    print s_save
except Exception as e:
    print e.__str__()
finally:
    print "----------"

# 模拟 POST 提交请求
import urllib

values = {'': "", '': ''}

data = urllib.urlencode(values)
req = urllib2.Request(url_save, data)
reponse = urllib2.urlopen(req)

the_page = reponse.read()

print "--->", the_page
