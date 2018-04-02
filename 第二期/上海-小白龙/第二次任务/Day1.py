#!/usr/bin/python
#encoding=utf-8
import math
import random
import cmath

__author__=u'小白龙'
class Numbers:
    def mathFuc(self):
        print(math.sqrt(9))#求平方
        print(math.fabs(-5))
        print(math.pi)#pai
        print(math.log10(100))
    def randomFuc(self):
        print(random.randint(1,10))#返回int数值
        print(random.random())#返回0-1之间的float型数值
        print(random.choice([u"小白龙",u"慧慧",u"五娃"]))#Return a random element from the non-empty sequence seq
    def cmathFuc(self):
        print(cmath.cos(45))
        print(cmath.log10(100))
        print(cmath.e)
class Strings:
    def StrFuc(self):
        str = "aabbbabcd"
        print(str.replace("aa","ee"))
        str2="123,abc,def,aaa"
        print(str2.split(","))#返回list
        print('-'.join(str2.split(",")))
        tuple1=('a','b','c')
        print('-'.join(tuple1))
        findstr=' fadslkfjw eir12343 '
        print(findstr.find('a'))
        print(findstr.lstrip())
        print(findstr.rstrip())
        print(findstr.strip())

        print('asd123'.isalnum())#判断字符是否有字母和数字组成
        print('asdf'.isalpha())#字母
        print('123'.isdigit())#数字
        print('asd'.islower())#小写字母
        print('ASDF'.isupper())#大写字母
        print('34'.isnumeric())#数字

class Tuples:
    def tupleFuc(self):
        """tuple用小括号()标识，元组的元素不可修改"""
        tuple1='a','b','c'
        print(tuple1)
        print(tuple1.__len__())
        print(tuple1[1])
        list =['12','ad','c']
        print(tuple(list))#list转换成tuple
        tuple2=('1','aaa')
        tuple3=tuple1+tuple2#元组合并
        print(tuple3)

class Lists:
    """List用中括号[]来标识,下标从0开始计算"""
    def listFuc(self):
        list1=[]
        for i in range(1,10):
            list1.append(i)#添加
        print(list1)
        print(len(list1))
        list1[2]=33
        print(list1)
        list2=[23,67]
        list1.extend(list2)#连接
        print(list1)
        list1.sort()#排序
        print("排序:"+str(list1))
        list4=list2.copy()#复制
        print(list4)
        list4.clear()#清空
        print(list4)
        list1.pop()#删除最后一个
        print(list1)
        list1.pop(3)#删除第四个
        print(list1)
        list1.remove(2)#删除第3个
        print(list1)

class Dictionarys:
    """
    字典Dictionary用中括号标识，其元素为key-value对应，key与value用冒号:分割开
    字典的key是唯一不可重复的，可以是数字，字符串，元组，但是不能是列表
    values可以是任何类型的对象
    """
    def dicFucs(self):
        dic1={'name':'小白龙',"age":18,"address":"上海"}
        print(dic1)
        print(dic1["name"],dic1.get("age"))
        print(dic1.keys())
        print(dic1.values())
        dic2=dic1.copy()
        print(dic2)
        dic3=dict.fromkeys(['age'],30)#创建一个字典,([keys],'defaultvalue')所有的key都是默认值，不设置默认值是为None
        dic2.update(dic3)#强dic3里的key-value更新到dic2里
        print(dic2)
        dic2.pop('address')#删除
        print(dic2)

class Sets:
    """set存储的元素：无序，不重复"""
    def setFucs(self):
        set1 =set([1,2,3])
        print(set1)
        set1.add('a')#add一次只能添加一个
        set1.add('b')
        print(set1)
        set1.remove('b')
        print(set1)
        set1.update([5,6,7])#update传入一个集合
        print(set1)


if __name__=="__main__":
    x = 12.83
    y = 3
    print(x)
    print(y)
    print(int(x))
    print(float(y))
    print(complex(x,y))
    print("==========math==========")
    num = Numbers()
    num.mathFuc()
    print("==========random==========")
    num.randomFuc()
    print("==========cmath==========")
    num.cmathFuc()
    print("==========Strings==========")
    strc = Strings()
    strc.StrFuc()
    print("==========Tuples==========")
    tup=Tuples()
    tup.tupleFuc()
    print("==========Lists==========")
    li=Lists()
    li.listFuc()
    print("==========Dictionarys==========")
    dic = Dictionarys()
    dic.dicFucs()
    print("==========Sets==========")
    sets = Sets()
    sets.setFucs()

