#修改import中的Queue为Manager
from multiprocessing import Manager,Pool
import os,time,random
def reader(q):
    print("reader启动(%s),⽗进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息： %s"%q.get(True))
def writer(q):
    print("writer启动(%s),⽗进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "dongGe":
        q.put(i)
if __name__=="__main__":
    print("(%s) start"%os.getpid())
    q=Manager().Queue() #使⽤Manager中的Queue来初始化
    po=Pool()
    #使⽤阻塞模式创建进程， 这样就不需要在reader中使⽤死循环了， 可以让writer完全执⾏完
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())