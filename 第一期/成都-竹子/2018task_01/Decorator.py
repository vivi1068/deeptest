#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
# _*_coding:utf-8 _*_
def Write(path):
    f = open(path, 'r')
    # list = []
    for i in f:
        list = i.strip().split(',')
        return list


login_status = False
def show_flag(auth_type):
    def login(f):
        def inner():
            global login_status
            f()
            if login_status == False:
                if auth_type=='jingdong':
                    print('调用京东程序....')
                    username = input('please input your username...')
                    password = input('please input your password...')
                    try:
                        account = Write('F:/ Interface/old boy/jingdong.txt')
                        if username == account[0] and password == account[1]:
                            print('Welcome to ....')
                            login_status = True
                        else: print('您输入的账号或者密码错误,请重新输入....')
                    except Exception as e:
                        print(e)

                elif auth_type=='weixin':
                    print('调用微信程序....')
                    username = input('please input your username...')
                    password = input('please input your password...')
                    try:
                        account = Write('F:/ Interface/old boy/wenxin.txt')
                        if username == account[0] and password == account[1]:
                            print('Welcome to ....')
                        login_status = True
                    except Exception as e:
                        print(e)
                else:
                    pass
            else:
                pass
        return inner
    return login

@show_flag(auth_type='jingdong')
def home():
    print('Welcome to home page')
# home()

@show_flag(auth_type='weixin')
def finance():
    print('Welcome to finance page')
finance()

@show_flag(auth_type='jingdong')
def book():
    print('Welcome to book page')