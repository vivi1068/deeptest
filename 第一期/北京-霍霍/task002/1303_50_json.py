# -*- coding:utf-8 -*-
__author__ = "huohuo"

import json

if  __name__ == "__main__":
    print("json串高级解析示例")
    json_demo = """
        {
            "weixin":[
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
            "web":[
                {
                    "url": "www.testingunion.com",
                    "name": "开源优测社区",
                    "desc": "分享各类开源测试技巧"
                },
                {
                    "url": "www.testingunion.com_demo",
                    "uid": "开源优测社区_demo",
                    "desc": "分享各类开源测试技术_demo"
                }
            ]
        }
    """
    # 将json串转换成字典
    json_dict = json.loads(json_demo)

    # 遍历字典
    for (k, v) in json_dict.items():
        # 输出第一层级，k 为weixin、web; v为其对应的列表即[]中的数据
        print(k, ":", v)
        for data in v:
            #遍历列表
            # v为[]
            for (data_k, data_v) in data.items():
                # 每个data为[]中的一个字典
                # 遍历列表中的字典
                print("  ",data_k, ":", data_v)   