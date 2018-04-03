# -*- coding: utf-8 -*-
# __author__ = 'Carina'


if __name__ == "__main__":

    # 1、创建元祖示例
    tuple1 = ('DeepTest', '开源优测', '1')
    tuple2 = (1, 2, 3, 4, 5)
    tuple3 = ("a", "b", "c", "d", "e")
    print("1、创建元祖示例")
    print(tuple1)
    print(tuple2)
    print(tuple3)
    print("*" * 50, "\n")     # 输出内容后换行

    # 2、内置函数
    print("2、内置函数")

    tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    # 计算元素个数
    print("计算tuple_demo的元素个数")
    print(len(tuple_demo))

    # 返回最大值
    print("返回tuple_demo中最大值的元素")
    print(max(tuple_demo))

    # 返回最小值
    print("返回tuple_demo中最小值的元素")
    print(min(tuple_demo))

    # 将list转换为元祖
    print("将list转换为元祖")
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple4 = tuple(tuple_demo)
    print(tuple4)

    print("*" * 50, "\n")

    # 3、切片
    print("3、元祖切片操作示例")

    data_demo = ("DeepTest", "appium", "testingunion.com", "hello", "python3")

    # 读取第二个元素appium，注意索引下标从0开始
    e = data_demo[1]
    print("读取第二个元素:", e)

    # 读取倒数第二个hello
    e = data_demo[-2]
    print("读取倒数第二个", e)

    # 切片，截取从第2个元素开始后的所有元素
    e = data_demo[1:]
    print("截取从第2个元素开始后的所有元素:", e)

    # 切片，截取第2-4个元素
    e = data_demo[1:4]
    print("截取第2-4个元素:", e)

    print("*" * 50, "\n")

    # 4、合并
    print("4、元祖合并或连接操作示例")
    tup1 = ("DeepTest", "appium")
    tup2 = ("testingunion", "hello", "python3")
    # 合并成新的元祖
    tup3 = tup1 + tup2
    print("合并前的元祖:", tup1, tup2)
    print("合并后的元祖：", tup3)

    print("*" * 50, "\n")

    # 5、删除
    print("5、元祖删除操作示例")
    tup4 =  ("DeepTest", "appium", "selenium")
    print("删除前的元祖内容：", tup4)
    # 删除元祖
    #del tup4['appium']
    #print("删除后的元祖内容：", tup4)

    print("*" * 50, "\n")

    # 6、运算
    print("6、元祖运算示例")
    tup5 =  ("DeepTest", "appium", "selenium", "FireFox")
    tup6 = (1, 2, 3, 4)
    # 计算元祖长度
    print("tup5的长度为：", len(tup5))
    # 元祖复制
    print("复制tup5三次：", tup5 * 3)
    # 判断元素是否在元祖中，是则返回True，否则返回False
    result = 5 in tup6
    print(" 5 in tup6：", result)
    # 遍历元祖
    print("遍历tup6:")
    for t in tup6 :
        print(t)

    print("*" * 50, "\n")

    # 7、方法
    print("7、元祖方法")
    names = ('mike', 'lucy', 'lily', 'lily', 'linda','lucas')
    print("count 计数：", names.count('lily'))
    print("index 索引：", names.index('linda'))
    print("index 索引：", names.index('lily'))    #计算第一个出现的值，从0开始




