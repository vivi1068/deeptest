# coding = utf-8
# 将json对象字符串存文件

import json

if __name__ == "__main__":
    print("python 写 json串实例")

    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    fp = open('json_write.json', 'w')

    # 以可读性格式写入json_wirte.json文件中
    json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ':'))

    fp.close()