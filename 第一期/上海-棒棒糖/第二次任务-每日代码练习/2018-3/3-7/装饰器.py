def w1(func):
    print('--正在装饰--')
    def inner():
        print('--正在验证权限--')
        func()
    return inner
@w1#只要执行到这行，自动进行装饰，而不是等待调用f1函数才装饰的
def f1():
    print('--f1--')

#f1()


import functools
def log(func):
    @functools.wraps(func)   # @functools.wraps意思是wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log     #等于执行了语句：now = log(now)
def now():
    print('2015-3-25')
now()


#定义函数： 完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
#定义函数： 完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test3())
