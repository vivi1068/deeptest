#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 10:50
# @Author  : yulu
# @File    : json_study
import json
if __name__ == "__main__":
    print("json 转 dict")

    json_str = '{"name" : "开源优测", "url" : "www.testingunion.com", "id" : "DeepTest"}'

    # 原生类
    print("原生类： ", type(json_str))

    # 转成 dict 对象
    # 会被转成字典类型
    json_dict = json.loads(json_str)
    print("转换后的类型：", type(json_dict))

    # 遍历字典
    for (k, v) in json_dict.items():
        print(k, ":", v)

    # 将字典转为 json串
    # 会被转为字符串类型
    dict_json = json.dumps(json_dict)
    print("json串: ", dict_json)
    print("类型： ", type(dict_json))

    # 解析一个复杂的json并遍历所有元素，打印出来
    print("json串高级实例： ")
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
    # 将json串转换成字典
    json_to_dict = json.loads(json_demo)
    # 遍历字典
    for (k1, v1) in json_to_dict.items():
        # 输出第一层级， k1为weixin, v1为 其对应的列表，即[]中的数据
        print(k1, ":", v1)
        for data in v1:
            # 遍历列表
            # v1 为 []
            for (data_k, data_v) in data.items():
                # 每个data为[]中的一个字典
                # 遍历列表中的字典
                print("   ", data_k, ":", data_v)