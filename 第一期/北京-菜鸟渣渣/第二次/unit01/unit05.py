# -*- coding:utf-8 -*-
from  collections  import  Iterable
from multiprocessing import  Process
import sys,os
print sys.argv[0]
print sys.path
print sys.version_info
print sys.subversion

sys.stdout.write("1000\n")

def worker(name):
    print name
    print 'parent process id:', os.getppid()
    print 'process id:', os.getpid()
if __name__ == '__main__':
    p = Process(target=worker, args=('function worker.',))
    p.start()
    p.join()
    print p.name


print os.name
__author__ = 'Young'
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

