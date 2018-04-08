# __author__ = 'wuwa'
# -*- coding:utf-8 -*-
import requests

from common.writeLog import mylogger


class requests_interface:
    def __init__(self):
        global result

    def __check_param(self, interface_params):

        if interface_params:
            return True
        else:
            return interface_params

    def __requet_get(self, interface_url, interface_param, headerdata):
        try:
            if interface_url != "" and interface_param != '':
                response = requests.get(url=interface_url, params=interface_param, headers=headerdata)
                if response.status_code == 200:
                    result = {'code': '0000', 'message': '成功', 'data': response.text}
                else:
                    result = {'code': '2004', 'message': '返回状态错误', 'data': []}
            elif interface_url == '':
                result = {'code': '2002', 'message': '请求地址为空', 'data': []}
            else:
                result = {'code': '1000', 'message': '请求类型错误', 'data': []}
        except Exception as error:
            mylogger.info(error)
        return result

    def __request_post(self, interface_url, interface_param, headerdata):
        try:
            if interface_url != '' and interface_param != '':
                response = requests.post(url=interface_url, data=interface_param, headers=headerdata)
                if response.status_code == 200:
                    result = {'code': 200, 'message': '成功', 'data': response.text}
                else:
                    result = {'code': 2004, 'message': '返回状态码错误', 'data': []}
            elif interface_url == '':
                result = {'code': '2002', 'message': '请求地址为空', 'data': []}
            else:
                result = {'code': '1000', 'message': '请求类型错误', 'data': []}
        except Exception as error:
            mylogger.info(error)
        return result

    def http_request(self, interface_url, interface_param, headerdata, request_type):
        try:
            if request_type == "get" or request_type == "GET":
                result = self.__requet_get(interface_url, interface_param, headerdata)
            elif request_type == "post" or request_type == "POST":
                result = self.__request_post(interface_url, interface_param, headerdata)
            else:
                result = {'code': '1000', 'message': u'请求类型错误', 'data': request_type}
        except Exception as error:
            result = {'code': '9999', 'message': u'系统异常', 'data': []}
            mylogger.info(error)
        return result


if __name__ == "__main__":
    interface_url = "你的请求url"
    interface_param ="请求参数"
    headers = "请求的头文件"
    res = requests_interface()
    result = res.http_request(interface_url, interface_param, headers, 'get')
    print(result)
