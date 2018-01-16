#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

class Fib:

    '''从无到有创建斐波那契数列'''

    def __init__(self,max):
        self.max=max

    def __iter__(self):
        self.a=0
        self.b=1
        return self

    def __next__(self):
        fib=self.a
        if fib>self.max:
            raise StopIteration
        self.a, self.b =self.b, self.a+self.b
        return fib


if __name__=='__main__':
    for n in Fib(1000):
        print(n,end=' ')
