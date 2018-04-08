# -*- coding:utf-8 -*-
import json


def json_t1():
    print("json转dic")
    
    '''
    json不能最外层不能随使用单引号，不能使用u''
    json_str="{ 'name':'你猜', 'url':'www.baidu.com', 'id':'id'}"
    '''
    json_str='{ "name":"你", "url":"www.baidu.com", "id":"id"}'
    print("json_str type ", type(json_str))

    json_dict = json.loads(json_str)

    print("json_list type ", type(json_dict))

    for v,k in json_dict.items():
        print(v,k)


def dict_t1():
    dict_1 = {"3":"33", "4":"44"}
    print("原类型：" , type(dict_1))  
    json_1 = json.dumps(dict_1)
    print("转换后的类型：", type(json_1))    
    print(json_1)

def json_dict():
    print("json串解析高级实例")
    json_demo ="""
        {
            "weixin": [
                {
                    "name": "开源优测",
                    "uid": "DeepTest",
                    "desc": "分享开源测试技术"
                },
                {
                    "name": "开源优测_demo",
                    "uid": "DeepTest_demo",
                    "desc": "分享开源测试技术_demo"
                }
            ],
            "web": [
                {
                    "url": "www.testingunion.com",
                    "name": "开源优测社区",
                    "desc": "分享各类开源测试技巧"
                },
                {
                    "url": "www.testingunion.com_demo",
                    "name": "开源优测社区_demo",
                    "desc": "分享各类开源测试技巧_demo"
                }
            ]
        }
    """
    dict1 = json.loads(json_demo)
    for v, k in dict1.items():
        #print(k,  " : " , v) 
        for x in k:
            for y ,z in x.items() :
                print(y,z)
        print("*"*60)




if __name__ == "__main__":

    json_t1()
    dict_t1()
    json_dict()
