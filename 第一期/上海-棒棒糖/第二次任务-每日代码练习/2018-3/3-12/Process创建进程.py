'''
from multiprocessing import  Process
import time

def test():
    while True:
        print('---test---')
        time.sleep(1)
p = Process(target=test)
p.start()


while True:
    print('---main---')
    time.sleep(1)


from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('Child process will start.')
p.start() #创建一个Process实例，用start()方法启动
p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
print('Child process end.')

'''



