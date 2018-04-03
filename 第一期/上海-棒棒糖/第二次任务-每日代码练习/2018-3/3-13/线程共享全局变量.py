import time
from threading import Thread

g_mun=100
def work1():
    global g_mun
    for i in  range(3):
        g_mun += 1
    print('---in work1 g_num is %d---'%g_mun)

def work2():
    global g_mun
    print('---in work2 g_num is %d---'%g_mun)

print('---创建进程前 g_num is %d---'%g_mun)
t1 = Thread(target = work1)
t1.start()

time.sleep(1)
t2 = Thread(target = work2)
t2.start()




from threading import Thread
import time

def work1(nums):
    nums=44
    print("----in work1---",nums)
def work2(nums):
#延时⼀会， 保证t1线程中的事情做完
    #time.sleep(1)
    print("----in work2---",nums)

g_nums = 66
t1 = Thread(target=work1, args=(g_nums,))
t1.start()
t2 = Thread(target=work2, args=(g_nums,))
t2.start()
