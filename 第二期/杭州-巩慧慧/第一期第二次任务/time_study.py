#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 18:39
# @Author  : yulu
# @File    : time_study
from  datetime import date
from datetime import time
from datetime import datetime
import time

if __name__ == "__main__":
    # 获取今天的日期
    today = date.today()
    print("今天是： %s" % today)

    # 把今天的日期年月日分开，重新格式化下
    print("今天是 %s %s %s" % (today.day, today.month, today.year))

    # 今天是星期几
    weekday_num = today.weekday()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("今天是：%s" % weekdays[weekday_num])

    # 此时
    today_now = datetime.now()
    print("现在时间： %s" % today_now)

    # 用time构造时间
    # t = time(hour=20, minute=15, second=2, microsecond=30)
    # print("构造时间： %s" % t)

    # 用datetime构造日期+时间
    d = datetime(year=2018, month=3, day=7, hour= 19, minute=0, second=0, microsecond=200)
    print("构造 日期+时间： %s" % d)

    # 默认格式化时间
    localtime = time.asctime(time.localtime())
    print("默认时间格式： %s" % localtime)

    # 格式化为：年-月-日 时：分：秒 星期几
    print("24小时格式化：", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    print("12小时格式化：", time.strftime("%Y-%m-%d %I:%M:%S %a", time.localtime()))

    # 带a.m. 或 p.m. 表示时间格式 %p
    print("带a.m. 或 p.m.24小时格式：", time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # 把时区也带上 %z
    print("带时区的时间格式： ", time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

