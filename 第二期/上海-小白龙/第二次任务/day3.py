#!/usr/bin/python
#encoding=utf-8
import sys
__author__='小白龙'

class Person:
    def __init__(self):
        self.name='aaa'
        print(u"Person初始化")
        #print('%d+%d=%d'%(a,b,a+b))
    def say(self):
        print('I am %s'%self.name)
class Shuaige(Person):
    def __init__(self,name,money):
        self.name=name
        #super(Shuaige,self).__init__() #调用父类构造方法
        Person.__init__(self)  #调用父类的未绑定的构造方法
        print(u'%s是个帅哥,有%d个亿！'%(name,money))
    def sayHi(self):
        print(u'我是个帅哥，你好啊，美女！')

    def iterFuc(self):
        tup=(1,2,3,4,5)
        iter_t=iter(tup)
        for i in iter_t:
            print(i,end=' ')
        print()
        list = [3,4,5,6]
        iter_l = iter(list)
        print('list 1:%d'%next(iter_l))
        print('list 2:%d'%next(iter_l))
        dict = {'name':"小白龙","age":"18","face":"帅哥脸"}
        iter_keys=iter(dict.keys())
        iter_values=iter(dict.values())
        while True:
            try:
                print('%s:%s'%(next(iter_keys),next(iter_values)))
            except StopAsyncIteration:
                sys.exit(0)
    def fibonacci(self):
        # 实现斐波那契数列
        a, b, count = 0, 1, 0
        while True:
            if count > 10:
                break
            yield a
            a, b = b, a + b
            count = count + 1
    def yieldFuc(self):
        f = self.fibonacci()
        while True:
            try:
                print(next(f), end=" ")
            except StopAsyncIteration:
                sys.exit(0)
    def readList(self):  #读取字符串，每次读取5个字符
        str = "13429374sdfjisdjfkdsf"
        index,count = 0,0
        for i in iter(str):
            print(i, end=" ")
            index = index + 1
            count = count + 1
            if count == 5:
                print()
                count = 0
                yield index

if __name__=='__main__':
    p1 = Person()
    p2 = Shuaige('小白龙',10)
    p2.say() #say是父类方法，say方法使用了name变量，调用父类构造方法时优先使用父类的name变量
    p2.sayHi()

    #p2.iterFuc()
    #p2.yieldFuc()

    y = p2.readList()
    while True:
        try:
            next(y)
        except StopAsyncIteration:
            sys.exit(0)