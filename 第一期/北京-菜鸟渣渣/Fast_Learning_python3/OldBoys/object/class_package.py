# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


class Bar:
    def add(self, content):
        print(self, self.name, self.age, content)

    def delete(self, content):
        print(self, self.name, self.age, content)

    def update(self, content):
        print(self, self.name, self.age, content)

    def get(self, content):
        print(self, self.name, self.age, content)
'''

obj = Bar()
obj.name = 'zhangsan'
obj.age = "23"
obj.add("添加")

obj.delete("删除")

obj.update("更新")

obj.get("查找")
'''
print("#" * 30)


########################################
# 构造方法
# obj = 类名()
# 1.创建对象
# 2.通过对象执行类中的一个特殊方法
'''
class Bar1:
    def __init__(self,name,age):
       
            # 构造方法
       
        print("123")
        self.name  = name
        self.age = age
        # b.name =name
        # b.age = age
        # print(b.name , b.age)

        # print(self.name,self.age)
    def add(self, content):
        print(self, self.name, self.age, content)


b = Bar1('alex',23)
b.url ="www"
b.head ='app'
# print(b)
# b.add("content")
        
'''
'''
class Bar1:
    def __init__(self,name,name2):
        self.name = name
        self.name2= name2

        # print(self.name,name2)

    def add(self, content):
        # print(self, self.name, self.age, content)
        print(self.name2)
cb1 = Bar1("zs1","zs2")
print(cb1.name)
cb1.add("contnets")

'''

class Person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
        self.o ="x"
        pass
        # self.n=name
        # self.a=age
    def  show(self):
        # print(self.n , self.name)
        print(self.name , self.age)
lihuan =Person("zhangasn",23)

lihuan.show()
print( lihuan.o)

