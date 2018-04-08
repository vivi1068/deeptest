#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")



''''
总结 :
1.如何创建类 
    class 类名 :
        pass
2.创建方法
    构造方法  __init__
        obj = 类名("al")
    普通方法
        obj = 类("xx")
        obj.普通方法名()
3.面向对象三大特性之一: 封装

class Bar:
    def __init__(self,n,a)
        self.name = n 
        self.age = a
        self.xue = "o"
b1 = Bar("alex" ,32)
b2 = Bar("alex" ,32)



4.试用场景
    如果多个函数中有相同的参数时, 转换成面向对象


5.面向对象三大特性之二 : 继承

1.继承
    class 父类:
        pass
    class 子类(父类):
        pass
    
2.重写
    防止执行父类中的方法
    
3.self 永远是执行该方法的调用者

4.父类和子类的方法都要执行
    super(子类,self).父类中的方法()
    父类名称.父类方法(self,...)


5. python支持多继承
    a.左侧优先
    b.一条道走到黑
    c.同一个根 ,根最后执行;


6.5.面向对象三大特性之三 : 多态
   =======>原生多态
   
    #Java 
    String v = 'alex'
    def func(String arg):
        print(arg)
    
    func('alex')
    func(123)
    
    #Python
        v = 'alex'
        def func(arg):
            print(arg)
        func(1)
        func('alex')


'''

####################中级#########################
'''
class Foo():
    #静态字段
    country ='中国'
    def  __init__(self,name):
        #普通字段 属于对象
        self.name = name


    #普通方法
    def show(self):
        print(self.name)


print(Foo.country)

obj = Foo("ls")
print(obj.country)
# print(Foo.name)
Foo.country = 'dongbie '

print(obj.country)

'''



'''
class Foo():
    def __init__(self):
        self.name = "a"
    def  bar(self):
        print("bar")

    @staticmethod
    def sta(arg):
        print(arg ,"234")
    @classmethod
    def classmd(cls , admin):
        #cls 是类名
        print("classmd" , admin)
# obj = Foo()
# obj.sta(11)
# Foo.sta("10")
#
# Foo.classmd("admin")
# obj.bar()
# Foo.bar(obj)
#
# print(obj.name)
# obj.show()
'''

'''
class Foo():
    def __init__(self):
        self.name = "a"
    def bar(self):
        print("bar")
    @property
    def per(self):
        print("123")
        return  1
obj = Foo()
r= obj.per
print(r)

'''

class Foo():
    def __init__(self):
        self.name = "a"

        self.name_list=['alex']
    def bar(self):
        print("bar")
    @property #用于获取数值 obj.per
    def per(self):
        del self.name_list[0]
        return self.name_list
    @per.setter  #用于赋值 obj.per ="xxx"
    def per(self,val):
        print(val)

    @per.deleter
    def per(self):
        print(666)

obj = Foo()
r = obj.per
print(r)

obj.per = 23
del obj.per




# 类成员:
# #1.字段(2种)
#     - 普通字段 保存在对象中 ,只能通过对象访问
#     - 静态字段 保存在内存中,且只保留一份;对象和类都可以进行访问
# #2.方法 (3种)
#     - 普通方法 :保存在类中, 有对象来调用 self =>对象
#     - 静态方法 :保存在类型,由类直接调用
#     - 类方法 : 保存在类型,由类直接调用 cls =>当前类

########应用场景
''' 
    如果对象中需要保存一些值,执行某功能的时候,需要对象中的值 使用普通方法
    不需要任何对象中的值, 使用静态方法

'''
#属性.特性

    # - 不伦不类






