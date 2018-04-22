# -*- coding: utf-8 -*-
# __author__ = 'Carina'

import json

if __name__ == "__main__":

    # json 转 dict
    print("json 转 dict")

    json_str = '{"name": "carina", "url": "https://www.jianshu.com/u/cebffa585c1b"}'

    # 原类型
    print("原类型：", type(json_str))

    # 转成dict对象
    # 会被转换成字典类型
    json_dict = json.loads(json_str)
    print("转换后的类型：", type(json_dict))

    # 遍历字典
    for (k, v) in json_dict.items():
        print(k, ":", v)

    for k in json_dict:
        print("%s :%s" % (k, json_dict[k]))


    # dict字典转json串示例
    print('dict 转json')

    json_dict1 = {"name": "carina",
                  "url": "https://www.jianshu.com/u/cebffa585c1b"}

    print('原类型：', type(json_dict1))

    # 将字典转换成json串
    # 会被转换成字符串类型
    json_str1 = json.dumps(json_dict1)

    print('转化后的类型：', type(json_str))
    print(json_str)


    # json串解析高级实例
    print("json串解析高级实例")
    json_demo = """
        {
        "weixin": [
        {
        "name": "carina",
        "url": "https://www.jianshu.com/u/cebffa585c1b"
        },
        {
        "name": "carina1",
        "url": "https://www.jianshu.com"
        }],
        "web":[
        {
        "url": "www.baidu.com",
        "name": "baidu"
        },
        {
        "url": "www.youku.com",
        "name": "youku"
        }
        ]
        }
        """
    # 将json串转换成字典
    json_dict = json.loads(json_demo)

    # 遍历字典
    for (k, v) in json_dict.items():
        # 输出第一层级, k 为 weixin、 web;  v 为 其对应的列表即 [] 中的数据
        print(k, ":", v)
        for data in v:
            # 遍历列表
            # v 为[]
            for (data_k, data_v) in data.items():
                # 每个data为[]中的一个字典
                # 遍历列表中的字典
                print(data_k, ":", data_v)
