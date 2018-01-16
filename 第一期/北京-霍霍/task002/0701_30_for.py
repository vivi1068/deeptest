# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    # for 遍历元组
    Tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    print("遍历元组，并打印出来：")
    for t in Tuple_1:
        print(t)

    # for 遍历列表
    list_1 = ["开源优测", "DeepTest", "快学python3"]

    print("遍历列表，并打印出来：")
    for text in list_1:
        print(text)

    # for 遍历字典
    dict_1 = {"开源优测":"DeepTest", "python":"快学python3"}

    print("遍历字典方式一，并打印：")
    for (key, value) in dict_1.items():
        print("%s : %s" % (key, value))

    print("-----------------")

    print("遍历字典方式二，并打印出来：")
    for key in dict_1:
        print("%s : %s" % (key, dict_1[key]))

    