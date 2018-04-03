import threading
# 调用threading.local()类，创建全局ThreadLocal对象:
local_school = threading.local()
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    # 绑定ThreadLocal的student属性
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread_A')
t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()

