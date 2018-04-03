import os
# 注意， fork函数， 只在Unix/Linux/Mac上运⾏， windows不可以
pid = os.fork()
if pid == 0:
    print('哈哈1')
else:
    print('哈哈2')
