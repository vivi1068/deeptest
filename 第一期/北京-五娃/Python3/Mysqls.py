# __author__ ='wuwa'
# -*- coding: utf-8 -*-
import random

import MySQLdb

"""
1、安装对应的数据库包
2、创建数据库连接
3、创建游标
4、增删改操作在执行execute操作后，需要在想数据库提交commit操作
"""

if __name__ == "__main__":
    # 连接数据库
    conn = MySQLdb.connect(host='172.16.3.34', user='root', passwd='yZT0b6m32UDg', db='interfacedb', port=3306,
                           charset='utf8')

    # 创建游标
    cur = conn.cursor()
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

    #  生成测试数据
    sql_data = []
    for index in range(0, 10):
        email = str(random.random()) + "@126.com"
        password = random.random()
        sql_data.append((email, password))

    # 执行sql语句
    cur.executemany(sql, sql_data)

    # 提交至数据库，select操作不需要commit操作
    conn.commit()

    # 取查询到的所有数据
    all_data = cur.fetchall()
    sql_all = "SELECT * FROM users"
    # 遍历打印出来
    rows = cur.execute(sql_all)
    if rows > 0:
        cur.scroll(0, mode='absolute')
        results = cur.fetchall()
        print results

    # 最后把数据库连接关闭
    conn.close()
