import os
import time

ret = os.fork()

if ret==0:
    print('子进程')
    time.sleep(5)
    print('子进程')
else:
    print('父进程')#父进程结束是命令行结束，等到执行子进程才会在命令行打印出内容
    time.sleep(3)

print('--over--') #先在父进程中等待3s执行，在在子进程中等待5s执行
