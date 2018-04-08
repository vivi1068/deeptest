# -*- coding: utf-8 -*-
# __author__ = 'Carina'

'''
# 写入文件
file = open('C:/Users/Carina/Desktop/last_name11','w')
file.write('hello world')
print(file)
'''


# 字符串合并
what_he_does = ' plays '
his_instrument = ' guitar '
his_name = 'Robert Johnson '
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)


# 不同数据类型合并
num1 = 1
string = '1'
num2 = int(string)
print(num1 + num2)


# 字符串相乘
words = 'hello world  ' * 3
print(words)

word = 'a looooooooooooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)


# 字符串的分片与索引
name = 'My name is LIly'
print(name[0])   #左侧起始字符串为0
print(name[-4])   #右侧开始算，最后一个为-1，往前找
print(name[11:14])   #从左11到14，不含14
print(name[11:15])
print(name[5:])   # 从左5到最后
print(name[:5])    #左边开始，到第四个
print(name[-4:-1])  # 输出右2到右4
print(name[-5:])   #倒数5位


# 隐藏手机号中间四位数字
phone_number = '13698741235'
hiding_number = phone_number.replace(phone_number[3:7],'*' * 4)
print(hiding_number)

#模拟手机通讯录中的号码联想功能
search = '168'
num_a = '13812016808'
num_b = '13299741235'
num_c = '16752394168'
print(search + ' is at ' + str(num_a.find(search)) + ' to ' +str(num_a.find(search) + len(search)) + ' of num_a')
# 包含子字符串就返回开始的索引值，否则返回-1
print(search + ' is at ' + str(num_b.find(search)) + ' to ' +str(num_b.find(search) + len(search)) + ' of num_b')
print(search + ' is at ' + str(num_c.find(search)) + ' to ' +str(num_c.find(search) + len(search)) + ' of num_c')


# 字符串格式化
print('{} a word she can get what she {} for.'.format('with','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'with',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('with','came'))
# 字符串填空应用
city = input("write down the name of city:")
url = "http://apistore.baidu.com/mocroservice/weather?citypinyin={}".format(city)






