import sys
# 生成器函数
# 实现斐波那契数列
def fib(n):
    a,b,count=0,1,0
    while True:
        if count>n:
            return
        yield a
        a,b=b,a+b
        count+=1
f=fib(10)
while True:
    try:
        print(next(f),end=' ')
    except StopAsyncIteration:
        sys.exit(0)

#利用生成器函数去读大文件，例如10G的文件，你可以利用生成器函数，
# 每次只读100M进行处理，处理完后再读取下一个100M，如此迭代下去
def read_log(file_path):
    BLOCK_SIZE=102400
    with open(file_path,'r')as f:
        while True:
            block=f.read(BLOCK_SIZE)  # 每次读取固定长度到内存缓冲区
            if block:
                yield block
            else:
                retrun  # 如果读取到文件末尾，则退出
file_path='/test/tset.log'
for block in read_log(file_path):
    print(block)