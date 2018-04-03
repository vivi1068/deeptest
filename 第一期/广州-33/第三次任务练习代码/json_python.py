# coding = utf-8
# 接口测试实例之json解析，基本示例

import json

if __name__ == "__main__":
    print("python json标准库解析实例")

    # python对象转json对象
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    json_data = json.dumps(data)

    # 打印出来看下效果
    print("转化前")
    print(type(data))
    print(data)
    print("-" * 40)
    print("转化后")
    print(type(json_data))
    print(json_data)

    # 将json对象转化成python对象

    python_data = json.loads(json_data)

    print()
    print("将json对象转化成python对象")
    print(type(python_data))
    print(python_data)
