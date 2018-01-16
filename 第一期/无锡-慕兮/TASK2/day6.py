# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import pymysql
import random

if __name__ == "__main__":
    print("PyMySql基本示例")

    #创建一个链接实例
    conn = pymysql.connect(
        host = "localhost",  # mysql服务ip地址，若服务在本机则用localhost
        port = 3306, # mysql服务端口
        user = "root",  # 访问mysql的用户名
        password = "",  # 访问mysql的密码
        db = "zentao",  # 默认连接到的数据库
        charset = "utf8"  # 连接字符集
    )
    try:
        # 创建用于交互的cursor对象
        cursor = conn.cursor()

        # 先插入10条测试数据
        # 构建插入数据的sql
        sql = "INSERT INTO `zt_user`(`account`, `password`, `role`) VALUES (%s, %s, %s) " #`加不加都可以

        # # 生成10条测试数据
        sql_data = []
        for index in range(0, 2):
            account = "%s"%random.choice("abcdefghijklmnopqrst")
            # pass1 = hashlib.md5()
            # pass1.update("tlq123456".encode())
            # password = pass1.hexdigest()
            password = "123456"
            role = "qa"
            sql_data.append((account, password, role))
        #
        # # 执行sql,进行批量插入数据
        '''
        print(sql_data)
        cursor.executemany(sql, sql_data)
        #
        # # 提交至数据库
        conn.commit()

        #查询5条数据
        sql = " SELECT * FROM zt_user "

        #执行sql
        cursor.execute(sql)

        #取查询到的所有数据
        all_data = cursor.fetchall()

        # #遍历打印所有数据
        # print("所有获得的数据")
        for data in all_data:
            print("id: %d account: %s password: %s" %
                  (data[0], data[2], data[3]))

        #取一条数据
        # 如果在fetchall 后执行fetchone，那么fetchone返回的值为空
        
        one_data = cursor.fetchone()
        if one_data:
            print("id: %d account: %s password: %s" %
                  (one_data[0], one_data[2], one_data[3]))
        '''

        #删除刚刚添加的数据
        sql = "DELETE FROM `zt_user` where `password` = '123456' "
        cursor.execute(sql)

    finally:
        # 最后把数据库连接关闭
        conn.close()