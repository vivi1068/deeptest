#! __author__ == 'wuwa'
# ! -*- coding:utf-8 -*-
import pymysql

from common.writeLog import mylogger

"""
创建数据库连接
"""


class pymysqlopreations:
    def __init__(self, host, port, user, password, db, charset='utf8', link_type=0):
        """
        link_type = 0 时，数据库返回结果为元组模式
        当link_type !=0时，数据库返回结果为字典模式
        :param host:
        :param port:
        :param user:
        :param password:
        :param db:
        :param charset:
        :param link_type:
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                        db=self.db, charset=self.charset)
            if link_type == 1:
                self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
            else:
                self.cur = self.conn.cursor()

        except Exception:
            mylogger.info(u'Mysql数据库连接失败！')

    def select_one(self, params):
        """
        查询一条数据
        :param params:
        :return:
        """
        try:
            self.cur.execute(params)
            result = self.cur.fetchone()
            result = {'code': '0000', 'message': u'执行单条查询操作成功', 'data': result}
        except:
            result = {'code': '9999', 'message': u'执行单条查询异常', 'data': []}
            mylogger.info(u'Mysql查询失败！')
        return result
        
    def select_all(self, params):
        """
        查询所有内容
        :param params:
        :return:
        """
        try:
            row = self.cur.execute(params)
            if row > 0:
                self.cur.scroll(0, mode='absolute')
                results = self.cur.fetchall()
                result = {'code': '0000', 'message': '执行查询所有数据成功', 'data': results}
            else:
                result = {'code': '0000', 'message': '执行查询所有数据成功', 'data': []}
        except:
            result = {'code': '9999', 'message': '执行查询所有数据异常', 'data': []}
            mylogger.info('Mysql查询多条数据失败！')
        return result

    def opt_one(self, params):
        """
        操作单条数据
        :param params:
        :return:
        """
        try:
            row = self.cur.execute(params)
            self.conn.commit()
            result = {'code': '0000', 'message': '执行单条数据成功', 'data': int(row)}
        except:
            result = {'code': '9999', 'message': '执行单条数据失败', 'data': []}
            mylogger.info('Mysql操作单条数据失败')
        return result

    def opt_many(self, stmt, data):
        """
        多条数据
        :param stmt:
        :param data:
        :return:
        """
        try:
            row = self.cur.executemany(stmt, data)
            self.conn.commit()
            result = {'code': '0000', 'message': '插入多条数据成功', 'data': int(row)}
        except:
            result = {'code': '9999', 'message': '插入多条数据失败', 'data': []}
            mylogger.info('Mysql 插入多条数据失败')
        return result

    def __del__(self):
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()


if __name__ == "__main__":
    conn = pymysqlopreations(host='127.0.0.1', port=3306, user='root', password='root', db='irootdb',
                             link_type=1)
       sql = " SELECT * FROM `interface_detail`"
    resutl = conn.select_one(sql)
    print(resutl)
    sql_demo = """ INSERT INTO `interface_detail`(NAME,detail,param,check_value,exe_env,LEVEL,require_login) VALUES('xx','xx','xx','id=10',0,0,0)"""
    roe = conn.opt_one(sql_demo)
    print(roe)
    results = conn.select_all(sql)
    print(results)
    updatestmt = ''' update `interface_detail` set LEVEL = %s where interface_id =%s'''
    data = [(5,18)]
    conn.opt_many(updatestmt,data)
    results = conn.select_all(sql)
    print(results)
