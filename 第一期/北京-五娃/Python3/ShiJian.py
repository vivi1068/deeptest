# __author__ ='wuwa'
# -*- coding: utf-8 -*-
from datetime import date, datetime
import time

today = date.today()
print ("今天是:", today)

# 格式化后打印
print("今天是 %s,%s,%s", (today.year, today.month, today.day))

# 看下今天是星期几
# 星期几    序号
# Monday     0
# Tuesday    1
# Wednesday  2
# Thursday   3
# Friday     4
# Saturday   5
# Sunday     6
# 通过weekday会获取到对应的序号，请根据序号对上上述表，来看是星期几
weekday_num = today.weekday()
print ("今天星期", weekday_num)

# 输出可读性更好的星期几
weekdays = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")
print("今天是 %s" % weekdays[weekday_num])

# 查看现在的时间
today_now = datetime.now()
print ('现在是', today_now)

# strftime函数
localtime = time.asctime(time.localtime())
print("当前默认日期时间格式: %s" % localtime)

# 格式化为： 年-月-日 时:分:秒 星期几
print("24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %A",
                                 time.localtime()))
print("12小时制缩写格式：", time.strftime("%Y-%m-%d %I:%M:%S %a",
                                  time.localtime()))

print("年月日-时分秒：",
      time.strftime(" %Y-%m-%d  %H:%M:%S", time.localtime()))
