__author__='棒棒糖'
#导入日期和时间
import time
from datetime import  date #date 仅用于日期处理（年、月、日）
from datetime import  time #time 仅用于时间处理（时、分、秒、毫秒）
from datetime import  datetime #datetime 可以处理日期和时间的组合（年、月、日、时、分、秒、毫秒）
if __name__=='__main__':
    #获取今天的日期
    today=date.today()
    print('今天是：%s'%today)
    #把今天的日期年月日分开，重新格式化一下
    print('今天是%s%s%s'%(today.day,today.year,today.month))
    # 星期几    序号
    # Monday     0
    # Tuesday    1
    # Wednesday  2
    # Thursday   3
    # Friday     4
    # Saturday   5
    # Sunday     6
    # weekday会获取到对应的序号
    weekday_num=today.weekday()
    print('今天weekday是%s'%weekday_num)
    #输出可读性更好的星期几
    weekdays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")
    print('今天weekday是%s' % weekdays[weekday_num])
    print('-'*30)

    #查看现在的时间
    today_now=datetime.now()
    print('现在是%s'%today_now)

    #用time来构造个时间
    t=time(hour=12,minute=20,second=30,microsecond=200)
    print('自己构造的时间是%s'%t)
    #构造日期时间
    d=datetime(year=2008,month=8,day=8,hour=8,minute=8,second=8)
    print('构造的日期时间是%s'%d)

    import time

    #格式化日期时间：strftime函数
    #当前时间格式
    localtime=time.asctime(time.localtime())
    print('当前默认时间格式：%s'%localtime)
    #格式化为 年-月-日 时:分:秒 星期几
    print('24小时制全格式:',time.strftime('%Y-%m-%d %H:%M:%S %A',time.localtime()))
    print('12小时制缩写格式',time.strftime('%Y-%m-%d %I:%M:%S %a',time.localtime()))
    # 带a.m. 或 p.m. 标识时间格式 和时区
    print('# 带a.m. 或 p.m. 24小时全格式：',time.strftime('%Y-%m-%d %H:%M:%S %p %a %z',time.localtime()))
    # 格式乱排下试试
    print('随意排格式：',time.strftime('%A %Y-%d-%m %p %H:%M:%S %z',time.localtime()))