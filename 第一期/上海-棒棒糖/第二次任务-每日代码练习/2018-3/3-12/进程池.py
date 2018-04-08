from multiprocessing import Pool
import os,time,random
def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    #random.random()随机⽣成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕， 耗时%0.2f"%(t_stop-t_start))

po=Pool(3) #定义⼀个进程池， 最⼤进程数3
for i in range(0,10):
    #Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))
    #三个三个执行，每次循环将会⽤空闲出来的子进程去调⽤⽬标
    po.apply_async(worker,(i,))

print("----start----")
po.close() #关闭进程池， 关闭后po不再接收新的请求
po.join() #等待po中所有⼦进程执⾏完成， 必须放在close语句之后
print("-----end-----")


