#!/usr/bin/python
# -*- coding: utf-8 -*-
#--author--:lee


# 题一：实现�一个四则运算的类，�要求实现任意两个数的�加减乘除运算
class Cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,other):  #特殊函数
        return self.a + self.b
    
    def __sub__(self,other):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b
    
    def mod(self):
        return self.a % self.b

print u'请输入两个数a和b进行加减乘除运算：'
print u'请输入a:'
a = input()  #输入正整数用input()，输入字符串用raw_input()
print u'请输入b:'
b = input()
cal = Cal(a,b)
print "a+b=",cal.__add__(cal) #初次使用类函数引用，少写了括号，导致运算值是地址。
print 'a-b=',cal.__sub__(cal)
print 'a*b=',cal.mul()
print 'a/b=',cal.div()
print 'a%b',cal.mod()
print 'a/b='+str(cal.div())
print 'a%b='+str(cal.mod())


#  题二：随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
import random

class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # �count为生成的随机数个数  
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.list = [random.randint(self.start,self.end) for _ in range(0, self.count)]

    # 实现排序，内部函数
    def __mysort__(self):
        print u'排序前随机数：\n',self.list
        count = len(self.list)
        print u'排序后的随机数：'
        for i in range(1, count):
            key = self.list[i]
            j = i - 1
            while j >= 0:
                if self.list[j] > key:
                    self.list[j+1] = self.list[j]
                    self.list[j] = key
                j -= 1
        return self.list

        

# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10,1000,100)

    # 打印排序后的结果
    print(sorted_data.__mysort__())

