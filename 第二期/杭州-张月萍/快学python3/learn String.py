# -*- coding: utf-8 -*-
# __author__ = 'Carina'


if __name__ == "__main__":

    # 1、引号创建字符串
    a = '我是字符串'
    b = "我是字符串"
    c = """我是字符串
    我是字符串
    我是字符串
    我还是字符串"""
    print("*" * 50)
    print("1、引号创建字符串")
    print(a)
    print(b)
    print(c)
    print("*" * 50)

    # 2、字符串的连接与分割
    print("\n2、字符串的连接与分割")
    t = ('1','2','3','4','5','6','7','a','b','c','efg','ws')

    # 用-将t中元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)
    print(type(str_demo))

    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)
    print(type(str_set))

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)
    print("*" * 50)

    # 3、字符串的查找与替换
    print("\n3、字符串的查找与替换")
    source_str = "it's my book.please show it，wa ka ka, yo yo you!"

    # 从左往右查找yo
    print("从左往右查找yo")
    print(source_str.find("yooo"))   # 找不到返回-1
    print(source_str.index("book"))

    # 从右往左查找yo
    print("从右往左查找yo")
    print(source_str.rfind("it"))
    # print(source_str.rindex("sbook"))    # 找不到抛出异常
    print(source_str.rindex("wa"))

    # 替换所有的yo
    des_str1 = source_str.replace("yo", "wahaha")
    print(des_str1)

    # 替换2次yo
    des_str2 = source_str.replace("yo", "wahaha", 1)
    print(des_str2)
    print("*" * 50)

    # 4、去除字符串前后空格
    print("\n4、去除字符串前后空格")
    demo_str = "    我的前   后 和 中 间 都有空格   "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    # 去除前后空格
    str = demo_str.strip()
    print(str)
    print("*" * 50)

    # 5、判断字符串类型
    print("\n5、判断字符串类型")
    str1 = "1234567890"
    str2 = "asdfghjklASDFGHJKL"
    str3 = "123456789qwertyuiopQWERTYUIOP"
    str4 = "qazwsxedc"
    str5 = "TYGHNYJMUKJ"
    str6 = "             "
    str7 = "   sdfgh  "
    str8 = "12"
    str9 = "See You Tomorrow"
    str10 = "see you tomorrow"
    str11 = "SEE You Tomorrow 明天见"
    str12 = "class"
    # isdigit 判断字符串是否都是数字，是则返回true,否则为false
    print(str1.isdigit())
    # isalpha,判断字符串是否都是字母，是则返回true,否则为false
    print(str2.isalpha())
    # isalnum，判断字符串是否由字母或数字组成，是则返回true,否则为false
    print(str3.isalnum())
    print(str11.isalnum())
    # islower 判断字符串是否都是小写，是则返回true,否则为false
    print(str4.islower())
    print(str3.islower())
    print(str5.islower())
    # isnumeric 判断字符串是否都是数字，是则返回true,否则为false
    print(str4.isnumeric())
    # isupper 判断字符串是否都是大写，是则返回true,否则为false
    print(str5.isupper())
    # isspace 判断字符串是否都是空格，是则返回true,否则为false
    print(str6.isspace())
    print(str7.isspace())
    # isdecimal 字符串是否只包含十进制字符，是则返回True，否则为False
    print(str8.isdecimal())
    # istitle 字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回rue，否则返回False
    print(str9.istitle())
    print(str10.istitle())
    print(str11.istitle())
    # isprintable 字符串中的所有字符都是可打印的，或者字符串是空的，则返回空，否则返回true
    print(str11.isprintable())
    print(str6.isprintable())
    # capitalize 首字母大写
    print(str4.capitalize())
    print(str11.isalnum())
    # isidentifier  字符串是一个有效的标识符，标识符和关键字,如class、def，返回true
    print(str12.isidentifier())
    print(str11.isidentifier())



