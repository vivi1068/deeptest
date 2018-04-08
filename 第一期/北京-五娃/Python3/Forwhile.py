# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
for 循环可以遍历任何序列，如列表、元组、集合、字符串、字典等
for 循环是一种迭代循环机制，所以in后面必须是一个序列
for var in 序列：
    代码块
break:结束当前循环，然后跳到下条语句
continue：结束当前循环，并忽略余下的语句，返回到循环的顶端，相当满足下一次迭代时，继续进行下一次迭代
方法 print_eachname 比方法 print_eachname_for_index要快
'''

nameList = ['Walter', 'Nicole', 'Steven', 'Henry']


def print_eachname():
    '''
    通过序列项迭代
    :return:
    '''

    for each in nameList:
        print(u'打印名字', each)


def print_eachname_for_index():
    '''
    通过序列的索引打印具体值
    :return:
    '''
    for each in range(len(nameList)):
        print(u'打印名字', nameList[each])


def while_for():
    '''
    while循环-语法：
    while 条件 ：
       代码块
    :return:
    '''
    print(u'打印九九乘法表')
    n = 1
    while n < 9:
        for i in range(n, 9):
            print('%d * %d =%2d' % (i, n, i * n), end='  ')
        print(" ")
        n = n + 1


def while_else(num):
    '''
    while与for循环中也可以使用else语句，是的，单独的使用else语句
    :return:
    '''

    count = num / 2
    while count > 1:
        if num % count == 0:
            print('%d的公约数%d' % (num, count))
            break
        count -= -1
    else:
        print(num)


def range_for_each():
    '''
    通过range()实现伪迭代
    range(stop) -> range object
    range(start, stop[, step]) -> range object
    功能：按照指定步长，生成一个指定范围的数值序列
    start ：数值序列起始数值，默认为0
    stop：数值序列终止数值
    step：数值序列中的数值的间距，默认为1
    注意：range生成的序列为闭开区间
    :return:
    '''
    for i in range(5):
        print(i)

    for i in (range(1, 10)):
        print(i)

    for i in (range(3, 21, 3)):
        print(i)


def print_each_dict():
    '''
    遍历字典的键值
    :return:
    '''
    dict_1 = {u"开源优测": u"DeepTest", u"python": u"快学Python3"}

    print(u'第一种方法：')
    for (key, vale) in dict_1.items():
        print(u'字典的key、value为：', '%s,%s' % (key, vale))

    print(u'第二种方法：')
    for key in dict_1:
        print(u'字典的key、value为：', '%s,%s' % (key, dict_1[key]))


if __name__ == '__main__':
    print_eachname()
    print_eachname_for_index()
    print_each_dict()
    range_for_each()
    while_for()
    while_else(10)
