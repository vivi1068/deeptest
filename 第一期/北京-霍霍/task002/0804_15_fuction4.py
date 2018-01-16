# -*- coding:utf-8 -*-
__author__ = "huohuo"

def str_join(str1, str2, str3):
    return str1 + str2 + str3

if __name__ == "__main__":
    print("字符串传参实例：")

    str1 = "大家好，"
    str2 = "我们的老师是："
    str3 = "苦叶子"

    str_j = str_join(str1, str2, str3)
    print(str_j)
    