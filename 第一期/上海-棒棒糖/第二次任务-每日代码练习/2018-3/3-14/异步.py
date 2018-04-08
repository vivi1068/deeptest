from multiprocessing import Pool
import time
import os
def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
        return "hahah"

def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)



if __name__=='__main__':
    pool = Pool(3)
    #使用funcfunc创建子进程，得到返回值"hahah"，主进程执行test2函数，传入参数"hahah"
    pool.apply_async(func=test,callback=test2)
    #主进程在循环中，得到返回值"hahah"，停下来执行test2函数，就是异步
    while True:
        time.sleep(5)
        print("----主进程-pid=%d----"%os.getpid())