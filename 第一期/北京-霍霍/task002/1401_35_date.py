# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 导入时期和时间
from datetime import date
from datetime import time
from datetime import datetime

if __name__ == "__main__":
    # 获取今天的日期
    today = date.today()
    print("今天是 %s " % today)

    # 把日期年月日分开，格式化
    print("今天是 %s %s %s" % (today.day, today.month, today.year))

    # 今天是周几
    # 序号Monday 0 Tuesday 1 Wednesday 2 Thursday 3 Friday 4 Saturday 5 Sunday 6
    weekday_num = today.weekday()
    print("今天weekday是 %s" % weekday_num)

    # 输出可读性更好的周几
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print("今天是 %s" % weekdays[weekday_num])
    print("-" * 30)

    # 当前时间
    today_now = datetime.now()
    print("现在是 %s" % today_now)

    # 用time构造时间
    t = time(hour = 12, minute = 20, second = 30, microsecond = 200)
    print("我们自己造的时间是 %s" % t)

    # 造日期
    d = datetime(year=2008, month=8, day=8, hour=8, minute=8, second=8)
    print("造的日期是 %s" %d)