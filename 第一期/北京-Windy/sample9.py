#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
import time

class Pause:

    '''暂停一秒输出并格式化当前时间'''
    '''利用python自带函数hex()实现将一个数的十六进制输出'''
    '''手动编写绝对值函数'''

    def __init__(self, x):
        self.x = x

    def pau(self):
        time.sleep(1)

    def abs(self):

        if self.x < 0:
            return -self.x
        else:
            return self.x


if __name__ == '__main__':
    li = [1, 2, 3, 'lisy']
    h = 900
    print("请输入一个数字：")
    p = Pause(int(input()))
    p.pau()
    print(li)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print("h的十六进制表示为：", hex(h))
    print("它的绝对值为：",p.abs())