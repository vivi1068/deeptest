# -*- coding:utf-8 -*-
__author__ = "huohuo"

import time

if __name__ == "__main__":
    #time.strftime(format[ , t])

    #先看下当前默认格式化的时间
    localtime = time.asctime(time.localtime())
    print("当前默认日期时间格式： %s" % localtime)

    # 格式化为：年-月-日 时：分：秒 星期几
    print("24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    print("12小时制缩写格式：",time.strftime("%Y-%m-%d %I:%M:%S %a",time.localtime()))

    # 带a.m.或p.m.标识时间格式%p
    print("带a.m.或p.m.24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # 把时区带上
    print("带时区的全格式：", time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # 格式乱排
    print("随意排格式：", time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))