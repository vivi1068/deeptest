# -*- coding:utf-8 -*-

__author__ = u'zhangjin'

if __name__ == "__main__":
    # 字典基本示例
    dict = {u"DeepTest": u"开源优测", u"book": u"快学Python3"}

    # 计算字典的长度
    print(len(dict))

    # 以字符方式输出字典,即将字典转换成字符串
    str_d = str(dict)
    print(str_d)
    print(dict)

    # 判断类型
    print(type(dict))  # 字典类型
    print(type(str_d))  # 字符串str类型