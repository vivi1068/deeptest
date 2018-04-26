# -*- coding: utf-8 -*-
# __author__ = 'Carina'


from datetime import date
from datetime import time
from datetime import datetime


if __name__ == "__main__":

    # 获取今天的的日期
    today = date.today()
    print("今天是 %s" % today)

    # 把今天的日期年月日分开，重新格式化下一下
    print("今天是 %s %s %s" % (today.day, today.month, today.year))

    # 看下今天是星期几
    # 星期几    序号
    # Monday     0
    # Tuesday    1
    # Wednesday  2
    # Thursday   3
    # Friday     4
    # Saturday   5
    # Sunday     6
    # weekday会获取到对应的序号，请根据序号对上上述表，来看是星期几
    weekday_num = today.weekday()
    print("今天weekday是 %s" % weekday_num)

    # 输出可读性更好的星期几
    weekdays = ('Nonday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satturday', 'Sunday')
    print("今天是 %s" % weekdays[weekday_num])

    # 获取当前时间
    today_now = datetime.now()
    print("现在是 %s" % today_now)

    # 用time构造时间
    t = time(hour=12, minute=15, second=30, microsecond=200)
    print("我们自己造的时间是 %s" %t)

    # 造日期与时间
    dt = datetime(year=2020, month=12, day=10, hour=12, minute=15, second=30, microsecond=200)
    print("我们自己造是日期时间 %s" % dt)
