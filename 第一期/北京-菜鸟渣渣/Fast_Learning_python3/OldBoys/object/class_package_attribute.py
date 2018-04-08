#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")



'''
###属性的表达方式 : 两种
'''

'''

class Bar:
    def foo(self,arg):
        print(self,arg,self.name,self.age)

z1 = Bar()
print(z1)
z1.name ="zhangsna"
z1.age =23
print(z1.foo(12))

print()
'''
# z2 = Bar()
# print(z2)
# print(z2 .foo(12))


'''
class Pergination:
    def __init__(self,current_page):
        try:
            p = int(current_page)
        except Exception as e:

            p=1
        self.page = p
    @property
    def start(self):
        val = (self.page -1)*10
        return val

    @property
    def end(self):
        val = (self.page ) * 10
        return val

li=[]
for i in  range(10000):
    li.append(i)
while True:
    p =input("请输入要查看的页码")
    obj =Pergination(p)

    # 1  0,10
    # 2  10,20
    # 3  20,30

    print(li[obj.start:obj.end])
'''
# 第二种方法
class Foo:
    def f1(self):
        return 123

    def f2(self , v):
        print(v)
    def f3(self):
        print("del")
    per =property(fget=f1,fset=f2,fdel=f3)

obj = Foo()
# ret = obj.per
#
# print(ret)

obj.per = 555

print(obj.per)

del obj.per