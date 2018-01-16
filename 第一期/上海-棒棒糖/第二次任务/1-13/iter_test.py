__author__='棒棒糖'
import sys
if __name__=='__main__':
    seq_tuple=(1,2,3,4,5)
    #使用iter创建迭代器
    seq_it=iter(seq_tuple)
    #使用next访问第一个元素
    print('第一个元素:%s'%next(seq_it))
    #访问第二个元素
    print('第二个元素:%s' % next(seq_it))
    #访问第三个元素
    print('第三个元素:%s' % next(seq_it))
    #使用for循环来遍历迭代器对象
    print('\nfor循环遍历迭代器对象：')
    for_it=iter(seq_tuple)
    for x in for_it:
        print(x,end='')
    #使用while结合next遍历迭代器对象
    print('\n\nwhile&next遍历迭代器对象：')
    while_it=iter(seq_tuple)
    while True:
        #当开始一个try语句后，在当前程序的上下文中作标记，
        # 当异常出现时就回到这里，try子句先执行
        # 接下来会发生什么依赖于执行时是否出现异常。
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()
