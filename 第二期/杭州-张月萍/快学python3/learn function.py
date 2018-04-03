# -*- coding: utf-8 -*-
# __author__ = 'Carina'

# 计算2个数相加
def sum(a, b):
    c = a + b
    return c

# 九九乘法表
def multi():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append("%d * %d = %2d" % (i, j, i*j))
        data.append(line)
    return data

# 元组传递
def sum_tuple(seq):
    total = 0
    for s in seq:
        total += s
    return total

# 字符串传递
def str_join(str1, str2, str3):
    return str1 + str2 + str3

# 创建文件
def text_create(name, msg):
    desktop_path = 'C:\\Users\Carina\Desktop'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')

# 敏感词过滤
def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)


if __name__ == "__main__":
    print("函数定义，计算和")
    # 调用函数
    c = sum(1, 2)
    print("1+2=", c)

    # 九九乘法表实例
    print("九九乘法表实例：")
    data = multi()
    for d in data:
        print(d)

    # 元组传参，求和实例
    print("元组传参，求和实例:")
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(tuple1)
    total = sum_tuple(tuple1)
    print("和为： %d" %total)

    #字符串拼接
    str1 = "today "
    str2 = "is "
    str3 = "Friday"
    str_j = str_join(str1, str2, str3)
    print(str_j)

    # 创建文件
    text_create('hello', 'hello world')

    #敏感词过滤
    t = text_filter('Python is lame')
    print(t)
