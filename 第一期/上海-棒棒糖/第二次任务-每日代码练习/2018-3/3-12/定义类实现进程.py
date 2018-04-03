from multiprocessing import Process
import time

class MyNewProcess(Process): 
    def run(self):  #重写父类中的run方法
        while True:
            print('---1---')
            time.sleep(1)

p=MyNewProcess()
p.start()     #调用父类的start方法会执行子类中的run方法

while True:
    print('---main---')
    time.sleep(1)