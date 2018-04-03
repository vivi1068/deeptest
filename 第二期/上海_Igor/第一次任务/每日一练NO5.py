#斐波那契数列,指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fib(number):
    a ,b = 0,1
    while number > a :
        print(a)
        a,b = b,a+b
    return a

print(fib(10))