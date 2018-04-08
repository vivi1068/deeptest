# -*- coding: utf-8 -*-
# __author__ = 'Carina'


# if示例
var1 =int(input("请输入一个整数："))
if var1 > 0 and var1 <10:
    print("你输入了一个大于0小于10的整数")
elif var1 >=10:
    print("你输入了一个大于等于10的整数")
else:
    print("你输入了一个负数")

# In 是否存在
string1 = "hello world"
if "he" in string1:
    print(True)
else:
    print(False)


# 密码功能演示
# 创建列表，保存用户密码
pwd_list = ['*#*#', '123456']
# 定义登录函数
def account_login():
    pwd = input('请输入密码：')
    # 用户输入的密码 等于 最新设定的密码，登录成功
    pwd_right = pwd == pwd_list[-1]
    pwd_reset = pwd ==pwd_list[0]
    if pwd_right:
        print("Login success!")
    elif pwd_reset:
        new_pwd = input("请输入新密码：")
        pwd_list.append(new_pwd)
        print("密码修改成功！")
        account_login()
    else:
        print("密码错误或者无效的输入")
        account_login()

if __name__ == "__main__":
    account_login()