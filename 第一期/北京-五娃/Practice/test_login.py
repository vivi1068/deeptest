# ！__author__ =='wuwa'
# ! -*- utf-8 -*-
import re

import pytest
import requests
import sys

from common.choiceEnv import choice_env
from common.pymysqlOpreation import pymysqlopreations
from libarry.httprequests import requests_interface

respons = requests_interface()
baseurl = choice_env('TEST')

conn = pymysqlopreations(host='172.16.0.0', port=3306, user='root', password='root', db='root',
                         link_type=1)


@pytest.fixture
def db():
    sql = " SELECT * FROM `interface_detail`"
    resutl = conn.select_all(sql)
    return resutl


@pytest.fixture(scope='module')
def login():
    url = "http://xx.xx.xx:xx/api/user/login?platform=mp"
    data = {"xxx": "xxx", "xxx": "xxx"}
    headers = {'content-type': "application/json"}
    r = requests.post(url, data, headers)
    value = re.findall(r'<Cookie token=(.*?) for', str(r.cookies))[0]
    token = 'token=' + value
    return token


def get_api_from_db(params):
    '''
    找到接口，并在数据库中查询出该条数据的信息
    :return:
    '''

    api_params = conn.select_one("SELECT * FROM `interface_detaill` WHERE detail = '%s'" % (params))
    return api_params


class TestClass:
    def test_api_user_info(self):
        apiprams = get_api_from_db('接口名')
        if apiprams['data'] == None:
            try:
                sys.exit(0)
            except:
                print('数据库中无此接口')
        else:
            url_interface = baseurl + str(apiprams['data']['detail'])
            querystring = apiprams['data']['param']
            headers = {'Cookie': login()}
            type_interface = apiprams['data']['type_interface']
            result = respons.http_request(interface_url=url_interface, interface_param=querystring, headerdata=headers,
                                          request_type=type_interface)
            assert '0000' == result['code']

    def test_api_role_set(self):
        apiprams = get_api_from_db('接口名')
        if apiprams['data'] == None:
            try:
                sys.exit(0)
            except:
                print('数据库中无此接口')
        else:
            url_interface = baseurl + str(apiprams['data']['detail']) + "?platform=mp"
            querystring = apiprams['data']['param']
            headers = {'Content-Type': 'application/json', 'Cookie': login()}
            type_interface = apiprams['data']['type_interface']
            result = respons.http_request(interface_url=url_interface, interface_param=querystring, headerdata=headers,
                                          request_type=type_interface)
            assert '0000' == result['code']

    def test_api_product_list(self):
        apiprams = get_api_from_db('接口名')
        if apiprams['data'] == None:
            try:
                sys.exit(0)
            except:
                print('数据库中无此接口')
        else:
            url_interface = baseurl + str(apiprams['data']['detail'])
            querystring = apiprams['data']['param']
            headers = {'Cookie': login()}
            type_interface = apiprams['data']['type_interface']
            result = respons.http_request(interface_url=url_interface, interface_param=querystring, headerdata=headers,
                                          request_type=type_interface)
            assert '0000' == result['code']

    def get_test_api_methods(self):
        '''
        获取类方法列表
        :return:
        '''
        return list(filter(lambda x: x.startswith('test_api') and callable(getattr(self, x)), dir(self)))


if __name__ == "__main__":
    # ['--html=./report.html', 'test_login.py']
    pytest.main(['--html=./report1.html', 'test_login.py'])
