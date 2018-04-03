#!/usr/bin/python3

import json

# json.loads  json.dumps
json_dic = {
    'age' : 25,
    'name' : 'CARLes',
    'hope' : 'sleeping',
    'toplue' : 20
    }

json_data = json.dumps(json_dic)
print(type(json_data), type(json_dic))

# 给文件写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(json_data, f) # 写入 JSON 数据

with open('data.json', 'r') as f:
    data = json.load(f) # 读取数据
    print(data)


# 复杂json
json_data1 = """
    {
    "weixin" : [
        {
            "gname" : "shop1",
            "gid" : 102312,
            "sid" : 78612
        },
        {
            "gname" : "shop2",
            "gid" : 102313,
            "sid" : 78613
        }
    ],
    "web" : [
        {
            "url" : "www.xxx.com",
            "wname" : "shopo",
            "lists" : "testjson"
        },
        {
            "url" : "www.xxx2.com",
            "wname" : "shopp",
            "lists" : "testsion"
        }
    ]
    }
"""
    
print(type(json_data1))
json_da = json.loads(json_data1)

for (k, v) in json_da.items():
    for (j, n) in v[0].items():
        print(j, n)
