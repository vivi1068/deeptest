# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
json.dumps 将python对象编码成json字符串，返回json字符串
json.loads 将已编码的json字符串解码为python对象，返回python对象的数据类型
Python类型         	Json
字典dict	          object
list列表、tuple元组	array
str字符串	          string
int、long、float	   number
True	              true
False	              false
None	              null

"""
import json

if __name__ == "__main__":
    print ("json to dict")
    json_str = '{"name": "开源优测", "url": "www.testingunion.com", "id": "DeepTest"}'
    print ("原始类型：", type(json_str))
    json_dict = json.loads(json_str)
    print ("原始类型：", type(json_dict))

    for key in json_dict:
        print (key, json_dict[key])

    print ("dict to json")
    json_dict_1 = {
        "name": "开源优测",
        "url": "www.testingunion.com",
        "id": "DeepTest"
    }
    print("原类型：", type(json_dict_1))
    # 将字典转换成json串
    # 会被转换成字符串类型
    json_str_1 = json.dumps(json_dict_1)
    print("转换后的类型：", type(json_str_1))
    print(json_str_1)

    print ("解析复杂json串 并遍历所有元素")
    json_demo = """
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
    # 将json串转为字典
    json_dict_2 = json.loads(json_demo)
    print (json_dict_2)
    # 将字典中的最外层的key value打印出
    for (k, v) in json_dict_2.items():
        print (k, ":", v)
        # 循环列表v的值
        for data in v:
            print (data)
            # 将v中的字典打印出来
            for k, v in data.items():
                print ("data_k,data_v", k, v)
