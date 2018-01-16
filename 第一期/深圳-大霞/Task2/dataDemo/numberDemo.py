__author__ = "大霞"#Number数字类型练习
import random
#Python3中的整型类似于Java中的BigInteger类型
if __name__ == "__main__":
    x=1.68
    y=10
    #将浮点数x转换为整数
    print(int(x))
    #将整数y转换为浮点数
    print(float(y))
    #将x转换为复数，实数部分为x 虚数部分为0
    print(complex(x))
    #将x转换为复数，实数部分为x 虚数部分为y
    print(complex(x,y))
    str='520'+'1314'
    print(str)
    data=520+1314
    print(data)
    #引入外援随机函数,random module里边的一个randint()函数1-10(大于等于1，小于等于10之间的随机数)
    secret=random.randint(1,10)
    print(secret)
    #int()、float()、str()紧密相关
    #浮点数
    a='520'
    b=int(a)
    print(a)
    print(b)
    c=5.99
    d=int(c)
    #type(数据)，获取数据类型信息
    print(c,type(c))
    print(d,type(d))
    print(type('520'))
    ble=True
    print(type(ble))
    