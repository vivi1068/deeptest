#!/usr/bin/python
#encoding=utf-8

import datetime
from datetime import date
import time

import json

class dateTimeHander:

    def function(self):
        today = date.today()
        print(today)
        print(today.year,today.month,today.day)
        weekday_num = today.weekday()
        list = ['monday','tuesday','wednessday','thursday','friday','saturday','sunday']
        print(weekday_num,list[weekday_num])

        today_now = datetime.datetime.now()
        print(today_now)
        t1 = datetime.time(hour=8,minute=24,second=32,microsecond=1234)
        print(t1)
        d1 = datetime.datetime(year=2008,month=8,day=12,hour=8,minute=24,second=32,microsecond=1234)
        print(d1)
    def formatTime(self):
        t = time.time() #获取当前时间戳
        print(t)
        localtime = time.localtime(t) #接收时间戳，返回元组
        print(localtime)
        t2 = time.mktime(localtime)
        print(t2)
        str = time.strftime("%Y-%m-%d %H:%M:%S %A",localtime)
        print(str)

class jsonParer:
    def func1(self):
        json_str = '{"name": "开源优测", "url": "www.testingunion.com", "id": "DeepTest"}'
        print(u'原类型：',type(json_str))
        #json转换成字典
        json_dict = json.loads(json_str)
        print(u'转后后：',type(json_dict))
        #遍历dictionary
        for (key,value)in json_dict.items():
            print(key,":",value)
    def func2(self):
        pass

if __name__=='__main__':
    dt = dateTimeHander()
    dt.function()
    dt.formatTime()

    jp = jsonParer()
    jp.func1()