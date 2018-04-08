def test():
    i=0
    while i<5:
        if i==0:
            temp=yield i
        else:
            yield i
        i+=1
        print(temp)
t=test()
print(t.__next__())
print(t.send('haha'))
print(t.send('hehe'))

def test1():
    while True:
        print('--1--')
        yield None
def test2():
    while True:
        print('--2--')
        yield None
t1=test1()
t2=test2()
while True:
    t1.__next__()
    t2.__next__()