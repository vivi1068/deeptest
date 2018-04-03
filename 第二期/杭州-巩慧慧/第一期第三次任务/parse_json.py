#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 13:00
# @Author  : yulu
# @File    : parse_json
import json

# json解析通用类
# 1.python_to_json
# 2.json_to_python
class ParseJson:
    def python_to_json(self, objname):
        json_data = json.dumps(objname, sort_keys=True, indent=4, separators=(',', ':'))
        return json_data

    def json_to_python(self, jsonname):
        data = json.loads(jsonname)
        return data


if __name__ == "__main__":

    parse_json = ParseJson()

    data = [{'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }]
    # 将 Python对象转化为json串
    print("转换前类型", type(data))
    json_data = parse_json.python_to_json(data)
    print("转换为json", type(json_data))
    print(json_data)
    data_one = parse_json.json_to_python(json_data)
    print("再次转换为Python", type(data_one))
    print(data_one)