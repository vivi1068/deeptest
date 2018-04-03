# coding = utf-8
# 从文件读取json格式的内容，转化为python对象

import json

if __name__ == "__main__":
    print("python读取json内容文件转化python对象实例")

    fp = open('json_write.json', 'r')

    python_data = json.load(fp)
    print(type(python_data))
    print(python_data)

    fp.close()