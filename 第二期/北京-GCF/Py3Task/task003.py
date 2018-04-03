# -*- coding:utf-8 -*-

__author__ = '高彩凤'

"""
    String（字符串），所有字符串为Unicode编码。
"""
if __name__ == '__main__':
    a = u'字符串'
    b = u"字符串"
    # 三引号可多行
    c = """字符串
    字符串
    字符串
    """
    print("a=", a, "b=", b, "c=", c)

    # 字符串内置函数
    """1. 字符串连接和切割:
        join(以指定的字符串将元组、列表中的所有的元素合并为一个新的字符串。)
        split(以指定的分隔符来截取字符串，返回一个list对象)
    """
    # 用-将t中元素合并成一个新的字符串
    t = ('1', '2', '3', '4', '5', 'a', 'b', 'efg')
    str_demo = '-'.join(t)
    print(str_demo)

    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)

    # 将t元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)

    """
        2. 字符串查找和替换
        find（find(str, beg=0, end=len(string)),查找str是否包含在字符串中，
        若指定了beg和end，则在beg和end范围中查找，若找到则返回开始的索引值，否则返回-1）
        index（同find方法，不同的是，index若未查找到，抛出一个异常信息，而不是返回-1）
        rfind（同find，但是从右边往左边查找）
        rindex（同index，但从右到左查找）
        replace（将字符串中指定的子串替换成目标字符串，如果指定了替换次数，则替换不超过指定的次数）
    """
    source_str = u"it's my book,please show it,wa ka ka, yo yo yo!"

    # 从左到右查
    print(u"从左到右查找yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右到左查
    print(u"从右到左查找yo")
    print(source_str.rfind("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的yo
    print(u"替换所有的yo")
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两个yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)

    """
        3.去除字符串前后空格
        lstrip：去除字符串左边的空格
        rstrip: 去除字符串右边的空格
        strip：去除字符串左右两边的空格，即把lstrip和rstrip都执行一遍
    """
    demo_str = " a bc d e f ghi  "
    rstr = demo_str.lstrip()
    print(rstr)
    lstr = demo_str.rstrip()
    print(lstr)
    str = demo_str.strip()
    print(str)

    """
        4.判断字符串类型
        isalnum：判断字符串是否由字母或数字组成，是则返回true,否则为false
        isalpha:判断字符串是否都是字母，是则返回true,否则为false
        isdigit、isnumeric:判断字符串是否都是数字，是则返回true,否则为false
        islower、ispace、isupper
    """
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "

    print(str_1.isalnum())
    print(str_2.isalpha())
    print(str_3.isdigit())
    print(str_4.isupper())
    print(str_5.islower())
    print(str_6.isspace())
    print(str_7.isspace())