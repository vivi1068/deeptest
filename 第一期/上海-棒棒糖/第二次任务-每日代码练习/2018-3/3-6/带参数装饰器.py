'''

def w1(func):
    print('--正在装饰--')
    def inner(*args,**kwargs):
        print('--正在验证权限--')
        func(*args,**kwargs)
    return inner
@w1#只要执行到这行，自动进行装饰，而不是等待调用f1函数才装饰的
def f1(a,b):
    print('--f1:a=%d,b=%d--'%(a,b))

f1(5,6)


import functools
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')   # now = log('DEBUG')(now)
def today():
    print('2015-3-25')
today()
print(today.__name__)


def w1(func):
    print('--正在装饰--')
    def inner(*args,**kwargs):
        print('--正在验证权限--')
        return func(*args,**kwargs)
    return inner
@w1#只要执行到这行，自动进行装饰，而不是等待调用f1函数才装饰的
def f1(a,b):
    print('--f1:a=%d,b=%d--'%(a,b))
    return 'haha'

ret=f1(5,6)
print(ret)



'''

import functools
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            if text=='DEBUG':
                 func(*args, **kw)
                 func(*args, **kw)
            else:
                 func(*args, **kw)
        return wrapper

    return decorator
#首先@logger('DEBUG')给logger函数传入参数，解释器读取到def decorator(func)这行，先不执行，返回return decorator的引用，这时候变成@decorator，开始装饰

@logger('DEBUG')
def today():
    print('today')

@logger('DEBUG2')
def today2():
    print('today2')

today()
today2()

