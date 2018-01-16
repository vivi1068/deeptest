# 0116学习python心得
## 1、关于函数

---

- 函数体内部的语句在执行时，遇到return语句，函数就执行结束并将结果返回
- 之前看不懂的pass，今天也终于理解了。pass可以理解为一个占位符，不影响函数的执行
- 定义函数的时候明确函数名和参数个数就可以了
- 定义函数的时候为了更加完善一点，可以对参数的类型进行判断
```
def my_abs(str):
    if not isinstance(str,(int,float)):
        raise TypeError("输入变量类型错误！")
    if str >= 0:
        return str
    else:
        return -str
```
- 生成随机数的内置函数为random
- random.randint(10,100)生成一个10-100之间的随机数，想要随机生成一个列表的话，需要使用    
```
for i in range(1, 101):
        mylist.append(random.randint(10, 1000))
```

```
 1 # coding=utf-8
 2 __author__ = 'Windy
 3 
 4 import random
 5 
 6 
 7 def testRand():
 8 
 9     # 在[a, b]之间产生随机整数 random.randint(a, b)
10     for i in range(5):
11         ret = random.randint(100, 999)
12         print("random.randint(100, 999) = {0}".format(ret,))
13 
14     # 在[a, b]之间产生随机浮点数 random.uniform(a, b)
15     for i in range(5):
16         ret = random.uniform(1.0, 100.0)
17         print("random.uniform(1.0, 100.0) = {0}".format(ret,))
18 
19     # 在[0.0, 1.0)之间产生随机浮点数 random.random()
20     for i in range(5):
21         ret = random.random()
22         print("random.random() = {0}".format(ret,))
23 
24     # 在样本population中随机选择k个 random.sample(population, k)
25     population = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" }
26     for i in range(5):
27         ret = random.sample(population, 3)
28         print("random.sample(population, 3) = {0}".format(ret,))
29 
30     # 在序列seq中随机选择1个 random.choice(seq)
31     seq = ("to", "be", "or", "not", 'tobe', 'is', 'a', 'question')
32     for i in range(5):
33         ret = random.choice(seq)
34         print("random.choice(seq) = {0}".format(ret,))
35 
36     # 从序列中随机获取指定长度的片断。不修改原有序列。
37     # random.sample(sequence, k)
38     sentence = "to be or not to be is a question"
39     for i in range(5):
40         ret = random.sample(sentence, 5)
41         print("random.sample(sentence, 5) = {0}".format(ret,))
42 
43     # 三角分布的随机数 random.triangular(low, high, mode)
44     for i in range(5):
45         ret = random.triangular(0, 100, 10)
46         print(" random.triangular(0, 100, 10) = {0}".format(ret,))
47 
48     # 高斯分布的随机数（稍快） random.gauss(mu, sigma)
49     for i in range(5):
50         ret = random.gauss(0, 1)
51         print(" random.gauss(0, 1) = {0}".format(ret,))
52 
53     # beta β分布的随机数 random.betavariate(alpha, beta)
54 
55     # 指数分布的随机数 random.expovariate(lambd)
56 
57     # 伽马分布的随机数 random.gammavariate(alpha, beta)
58 
59     # 对数正态分布的随机数 random.lognormvariate(mu, sigma)
60 
61     # 正态分布的随机数 random.normalvariate(mu, sigma)
62 
63     # 冯米塞斯分布的随机数 random.vonmisesvariate(mu, kappa)
64 
65     # 帕累托分布的随机数 random.paretovariate(alpha)
66 
67     # 韦伯分布的随机数 random.weibullvariate(alpha, beta)
68 
69 
70 if __name__ == "__main__" :
71     testRand()
```
## 2、 关于类

---
- 实例化类的时候，如果定义了__init__()函数且该函数有参数，那么在访问类的属性或方法的时候也需要给相同个数和类型的参数，但是self不需要手动传参
- 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例均拥有相互独立的数据，互不影响
- 方法就是与实例绑定的函数，和在类之外定义的函数不同，方法可以直接访问实例的数据
- python允许同一个类的两个实例拥有不同的名字