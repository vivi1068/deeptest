#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


class F:
    def f1(self):
        print("F:f1")
    def f2(self):
        print("F:f2")


class S(F):
    def s1(self):
        print("S:s1")
    def f2(self):
        print("S:s2")
        # super(S,self).f2() #执行父类或者基类中的方法
        F.f2(self)           #执行父类的方法
#

# obj =  S()
# obj.f1()
# obj.f2()

obj = S()
obj.f2()