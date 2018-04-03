# __author__ = 'wuwa'
# -*- coding:utf-8 -*-

"""
1、大小写敏感
2、缩进表示层级关系
3、缩进时不允许使用Tab健，只允许使用空格
4、缩进空格数据不重要，相同层级的元素，左侧对齐即可
5、#注释
数据结构
1、对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
2、数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
3、纯量（scalars）：单个的、不可再分的值。字符串、布尔值、整数、浮点数、Null、时间、日期
"""
import codecs

import yaml

if __name__ == "__main__":
    print("yaml示例")
    document = """
    公众号: 开源优测
    基本信息:
        创建人: 苦叶子
        id: DeepTest
    """

    # 将yaml格式内容转为dict,使用load方法
    load = yaml.load(document)
    print(type(load))
    print(load)

    # 将python对象转为ymal格式
    output = yaml.dump(load, stream=None)
    print(type(output))
    print(output)

    # 多行yaml格式的解析

    print("python yaml 多行内容解析")
    f = codecs.open('ymalDemo.yaml', 'r', 'utf-8')
    document = f.read()
    f.close()
    load = yaml.load_all(document)
    print(load)
    for data in load:
        print(type(data))
        print(data)

        # 将python转为yaml格式
        print("---" * 25)
        output = yaml.dump(data)
        print(type(output))
        print(output)
