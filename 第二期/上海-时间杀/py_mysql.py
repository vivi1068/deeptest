#!usr/bin/python3

import pymysql
import random
import time

host = "xxx.xxx.xxx.xxx"
db_user = "xxx"
db_pass = "xxx"
db_name = "xxx"

# 连接数据库
db = pymysql.connect(host,  # 服务器地址
                     port=3306, # 数据库服务器端口
                     user=db_user,  # 连接mysql用户名
                     password=db_pass,  # 连接mysql密码
                     db=db_name,    # 要连接的数据库
                     charset="utf8"
                     )    

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据
data = cursor.fetchone()

print(data)


# 批量执行sql

try:
    for i in range(10):
        cid = "xxx"
        bid = 'xxx%d' % (i)
        date = time.strftime("%Y-%m-%d", time.localtime())
        sql = "INSERT INTO xxx (`cs_id`,\
 `buyer_id`, `date`, `shop_id`, `num`)\
 values ('%s', '%s', '%s', 'xxx', '-1')" % (cid, bid, date)
        print(sql)
        cursor.execute(sql)
except BaseException as e:
    print(e)


db.commit()

sql = "select * from xxx where shop_id = xxx\
     and date = '2018-3-30'"
cursor.execute(sql)

all_data = cursor.fetchall()
if len(all_data) == 10:
    for data in all_data:
        print(data)
else:
    print(len(all_data))

sql = "delete from xxx where shop_id = xxx\
     and date = '2018-3-30'"
cursor.execute(sql)
db.commit()

db.close()
