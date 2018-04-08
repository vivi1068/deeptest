#-*- coding:utf-8 -*-
import pymysql
import random

if __name__ == "__main__":

    cnn = pymysql.connect(
        host= '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '222222',
        db='test',
        charset='utf8')

    try:
        cursor = cnn.cursor()
        sql = "create table if not exists  user(email varchar(50), password varchar(50));"
        cursor.execute(sql)
        sql_set = "insert into user(email,password) values(%s,%s)"

        sql_data = []
        for index in range(10):
            email = "%10f@126.com"%random.random()
            password = str(random.random())
            sql_data.append((email,password))

        cursor.executemany(sql_set, sql_data)
     
        cnn.commit()

        sql_s = "select * from user;"
        cursor.execute(sql_s)
        all_data = cursor.fetchall()

        for data in all_data:
            print("email:%s, password:%s"%(data[0],data[1]))
        
        print("*" * 30)
        cursor.execute(sql_s)
        data = cursor.fetchone()
        print(data)

    finally:
        cnn.close()



