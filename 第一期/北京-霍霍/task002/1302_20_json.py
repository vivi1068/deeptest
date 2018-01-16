# -*- coding:utf-8 -*-
__author__ = "huohuo"

import json

if __name__ == "__main__":
    print("字典转换成json串")

    json_dict = {
        "name": "开源优测",
        "url": "www.testingunion.com",
        "id": "DeepTest"
    }

    print("原类型：", type(json_dict))

    # 将字典转换为json串
    json_str = json.dumps(json_dict)

    print("转换后的类型：", type(json_str))
    print(json_str)