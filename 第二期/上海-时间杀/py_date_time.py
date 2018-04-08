#!/usr/bin/python3

import time
import calendar
import datetime

times = time.time() # 时间戳单位最适于做日期运算
localtimes = time.localtime(times) # Python用一个元组装起来的9组数字处理时间
# localtimes = time.asctime(localtimes) # =ctime
print(times)
print(localtimes)

times = time.ctime()
print(times, ' ', times[0])

# 格式化日期
print(time.strftime("%Y-%m-%d %M:%S:%H %A", time.localtime()))
print(time.strftime("%I:%M:%S %p %Y-%m-%d", time.localtime()))

# time.sleep(5)

cal = calendar.month(1991, 3)
print("\n1991年3月份的日历:")
print(cal)


# datetime
today = datetime.date.today()
print(today)
print(today.day, today.month, today.year, today.weekday())
