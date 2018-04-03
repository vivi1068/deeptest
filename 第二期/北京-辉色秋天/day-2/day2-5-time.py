#-*-coding:utf-8-*-

from datetime import date
from datetime import time
from datetime import datetime

def datetime_test():
    today = date.today()
    print("今天是%s"%today)

    print("今天是%s,%s,%s"%(today.year,today.month,today.day))

    week_num = today.weekday()
    weekdays=("monday",'tuesday',"wednesday","thursday",'friday','saturday',"sunday")
    print(weekdays[week_num])


    print("*"*60)
 
    time_now = datetime.now()
    print("现在是%s"%time_now)

    time_c = time(hour=12,minute=12,second=12,microsecond=12)
    print("the time we created is %s"%time_c)


    time_c1 = datetime(year=1990,month=7,day=4,hour=12,minute=12,second=12)
    print("the time we created is %s"%time_c1)





if __name__ =="__main__":
    datetime_test()
