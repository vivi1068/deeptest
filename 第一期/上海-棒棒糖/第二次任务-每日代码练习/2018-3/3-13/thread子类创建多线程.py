import threading
import time

class Mythread(threading.Thread):
    #重写父类中的run方法
    def run(self):
        for i in range(3):
            time.sleep(1)
            # 调用父类中name属性，保存的是当前线程的name，Thread-
            msg="I'am "+self.name+' @'+str(i)
            print(msg)
if __name__=='__main__':
    t=Mythread()
    #调用父类中start方法，执行子类中run方法
    t.start()