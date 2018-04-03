# -*- coding: utf-8 -*-
# __author__ = 'Carina'


if __name__ == "__main__":
    # for 元组遍历
    tuple_1 = (1, 2, 3, 4, 5, 6)
    print("遍历元组并打印出来：")
    for t in tuple_1:
        print(t)

    # for 列表遍历
    list_1 = ['appium', 'selenium', 'Postman', 'Jmeter']
    print("遍历列表并打印出来：")
    for l in list_1:
        print(l)

    # for 遍历字典
    dict_1 = {"a": "appium", "s": "selenium", "p": 'Postman', "j": "Jmeter"}
    print("遍历字典方式一并打印出来：")
    for (key, value) in dict_1.items():
        print("%s : %s" % (key, value))   # %s,表示格化式一个对象为字符

    print("\n-----------------------")

    print("遍历字典方式二并打印出来：")
    for key in dict_1:
        print("%s : %s" % (key, dict_1[key]))

    # range函数示例
    print("range for 循环实例")
    # 使用默认参数生成序列进行遍历
    for i in range(5):
        print(i, end=",")
    # 换行
    print("")
    # 指定范围生成序列进行遍历
    for i in range(0, 10):
        print(i, end=",")
    # 换行
    print('')
    # 带步长方式生成序列进行遍历
    for i in range(0, 10, 2):
        print(i, end=",")

    # 循环列表时获取元素索引
    letters = ['a','b','c','d','e','f','g']
    for num1,letter in enumerate(letters):
	    print(letter, 'is',num1+1)

    # 九九乘法表
    for i in range(1, 10):
        for j in range(1, 10):
            # %d表示整数
            # %2d是将数字按宽度为2，采用右对齐方式输出，若数据位数不到2位，则左边补空格
            #print("%d * %d = %2d" % (i, j ,i*j), end="  ")
            print('{} * {} * {}'.format(i, j,i*j), end="   ")
        print("")

    # for 与 if 结合
    # 根据歌名打印歌手
    songslist = ['Holy Diver', 'Thumderstruck', 'Rebel Rebel']
    for song in songslist:
        if song == 'Holy Diver':
            print(song, '- Dio')
        elif song == 'Thumderstruck':
            print(song, '- AC/DC')
        elif song == 'Rebel Rebel':
            print(song, '- David Bowie')

    # 输出0-100之间的偶数
    for i in range(1,100):
        if i % 2 == 0:
            print("输出0-100之间的偶数：", i, end="  ")
            i +=1
        else:
            i +=1