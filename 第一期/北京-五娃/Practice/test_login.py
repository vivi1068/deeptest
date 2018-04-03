# ！__author__ =='wuwa'
# ! -*- utf-8 -*-
import re

import pytest
import requests

from common.choiceEnv import choice_env
from common.pymysqlOpreation import pymysqlopreations
from libarry.httprequests import requests_interface

respons = requests_interface()
baseurl = choice_env('TEST')

@pytest.fixture
def db():
    conn = pymysqlopreations(host='xxx', port=xxx, user='xxx', password='xxx', db='xxx',
                             link_type=1)
    sql = " SELECT * FROM `interface_detail`"
    resutl = conn.select_all(sql)
    return resutl

@pytest.fixture(scope='module')
def login():
    url = "http://xxxx"
    data = {"xxx": "xxx", "xxx": "xxx"}
    headers = {'content-type': "application/json"}
    r = requests.post(url, data, headers)
    value = re.findall(r'<Cookie token=(.*?) for', str(r.cookies))[0]
    token = 'token=' + value
    return token


class TestClass:
    def test_insurance_interface(self, login,db):
        """
        测试接口
        :param login:
        :return:
        """
        results = db
        print(db)
        print("============================")
        if len(results['data']) != 0 and results['code'] =='0000':
            for temp_case_interface in results['data']:
                print(temp_case_interface)
                url_interface = baseurl + str(temp_case_interface['detail'])
                querystring =temp_case_interface['param']
                headers = {'Cookie': login}
                type_interface = temp_case_interface['type_interface']
                result = respons.http_request(interface_url=url_interface, interface_param=querystring, headerdata=headers,
                                 request_type=type_interface)
                print(result)
                print("<<<<<<<<<<<<<<<<<<<<<<")



if __name__ == "__main__":
    # ['--html=./report.html', 'test_login.py']
    pytest.main(['--html=./report1.html', 'test_login.py'])
