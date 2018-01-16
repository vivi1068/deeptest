# coding=utf-8
__author__ = 'Young'

from threading import Thread, current_thread, Lock
import  urllib,re,urllib2
'''
# This module is just a placeholder for possible future expansion, in
# case we ever want to augment the stuff in _db in any way.  For now
# it just simply imports everything from _db.
'''

# simultat multiplay thread
global lock
lock = Lock()


#req = urllib2.urlopen('http://www.imooc.com/course/list')
req= urllib2.urlopen("http://www.imooc.com/course/list")
buf = req.read()
print buf


listurl =re.findall(r'http:.+\.jpg',buf)
print listurl

i=0
for url in listurl:
    f = open(str(i)+'.jpg','w')
    # req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1



class myThread(Thread):
    i = 0

    def __init__(self, n):
        super(myThread, self).__init__()
        self.n = n


    def run(self):
        print  "Current_thread Name %s" % current_thread().name
        self.i = self.n + 1
        print "indexNum", self.n, self.i

    def thread_work(self):
        print  "Current_thread Name %s" % current_thread().name
        print "indexNum", self.n

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getImg(html):
#re.compile('.*g_img={url: "(http.*?jpg)"', re.S)
    reg = ""
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

if __name__ == "__main__":
    for index in range(5):
        lock.acquire()
        t = myThread(index)
        t.start()

        t.join()
        lock.release()

html=getHtml("http://www.cnblogs.com/fnng/p/3576154.html")
print "---->Image",getImg(html)
'''
http://images.cnblogs.com/cnblogs_com/fnng/835722/o_pyif_book.jpg

'''

str='''
http://images.cnblogs.com/cnblogs_com/fnng/835722/
'''