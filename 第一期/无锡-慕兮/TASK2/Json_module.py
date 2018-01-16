# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import json

if __name__ == "__main__":
    print("json 转 dict")

    json_str = '{"name": "开源优测", "url": "http://www.testingunion.com", "id": "DeepTest"}'

    #原类型
    print("原类型：", type(json_str))

    #转换成dict对象
    json_dict = json.loads(json_str)
    print("转换后的类型：",type(json_dict))

    for k, v in json_dict.items():
        print("%s :%s"%(k,v))

    print("字典转json串")

    dict = {"name": "ka iyuan you ce", "id": "DeepTest", "author": "dashi"}
    json_dict1 = json.dumps(dict)
    print("转换后的类型：", type(json_dict1))
    print(json_dict1)