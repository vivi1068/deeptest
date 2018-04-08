# -*- coding:utf-8 -*-
import sys
__author__ = '高彩凤'

if __name__ == "__main__":
    # 1.注释方式
    sum = 0
    for index in range(1, 100):
        sum = sum + index
    '''
    多行注释
    '''
    print("1-99的和为:%d" % sum)

    # 2.读取键盘输入
    data = input("请输入任意字符：")
    print("你输入了：%s" % data)

    # 3.通过空格切割输入的字符串
    list_data = data.split(' ')
    print(list_data)

    # 4.命令行参数,在teiminal进入当前目录下输入python3 task001 参数执行
    print("命令行参数个数：%d" % len(sys.argv))
    print("命令行参数列表：%s" % str(sys.argv))


