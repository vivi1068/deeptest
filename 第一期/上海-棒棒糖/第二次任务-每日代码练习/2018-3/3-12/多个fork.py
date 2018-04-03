import os
import time
pid = os.fork()
if pid == 0:
    #子进程
    print('哈哈1')
else:
    #父进程
    print('哈哈2')
    pid = os.fork() #父进程在这里是主进程，产生另外的父进程和子进程
    if pid == 0:
        print('哈哈3')
    else:
        print('哈哈4')
    time.sleep(1)