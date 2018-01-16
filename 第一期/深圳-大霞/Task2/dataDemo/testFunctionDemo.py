__author__ = "大霞"
import math #数学函数
import random#随机函数
import cmath #三角函数
if __name__ == "__main__":
    x=-100
    y=1.9
    #取绝对值函数abs（x）
    print(abs(x))
    #返回最大值
    print("最大值：")
    print(max(x,y))
    #返回最小值
    print("最小值：")
    print(min(x,y))
    #返回平方根
    print("平方根：")
    print(math.sqrt(y))

    #随机函数random模块中
    #常用随机函数
    print(u'常用随机函数')
    a=[1,2,3,4,5,6,7,8]
    #从a列表中随机选取一个数值
    print(random.choice(a))
    #从指定的范围（2-100按递增5的数据集）中随机选取一个
    print("从指定的范围（2-100按递增5的数据集）中随机选取一个:")
    print(random.randrange(2,100,5))
    #生成一个随机数，它在0-1之间
    print("生成一个0-1之间的随机数：")
    print(random.random())
    print(random.randint(1,10))#生成一个1-10之间的随机整数


    #常用的三角函数
    print(u"常用的三角函数：")
    x=100
    #返回x的返余弦函数值
    print(u"x的返余弦函数值:")
    print(cmath.acos(x))
    #返回x的余弦弧度值
    print(u"返回x的余弦弧度值")
    print(cmath.cos(x))
    #返回x的正弦弧度值
    print(u"返回x的正弦弧度值:")
    print(cmath.sin(x))

    #数学常量
    print(u"数学常量：")
    print(cmath.pi)