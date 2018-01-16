# -*- coding:utf-8 -*-
__author__ = "huohuo"

import json

if  __name__ == "__main__":
    print("json转为dict")

    json_str = '{"name" : "开源优测", "url":"www.testingunion.com", "id":"DeepTest"}'

    # 原类型
    print("原类型:", type(json_str))

    # 转换为dict对象
    # 会被转换为字典类型
    json_dict = json.loads(json_str)
    print("转换后的类型:", type(json_dict))

    # 遍历字典
    for(k, v) in json_dict.items():
        print(k, ":", v)
