#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 19:39
# @Author  : yulu
# @File    : mysql_study
import pymysql
import random

if __name__ == "__main__":
    print("PyMySQL基本示例")

    # 创建一个连接实例
    connect = pymysql.connect(
        host="192.168.199.30",
        port="3306",
        user="root",
        password="aWSkpQvyOEq6",
        db ="amg_mkt_activity_1",
        charset="utf8"
    )
    try:

        cursor = connect.cursor()
        sql = "SELECT * FROM amg_mkt_0.amg_mkt_activity_1 WHERE activity_id = 137199531183255553"
        cursor.execute(sql)
        results = cursor.fetchall()
        print("结果集： ", results)
        # for result in results:

    finally:
        connect.close()