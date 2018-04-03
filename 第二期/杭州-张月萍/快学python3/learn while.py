# -*- coding: utf-8 -*-
# __author__ = 'Carina'

# while 循环
#print("计算0-100间所有偶数和")
n = 100
index = 0
sum = 0
while index < n:
    sum += index
    index += 2
print("0-100间的偶数和=%d" % sum)

# while 与 for 综合使用
print("九九乘法表示例")
n1 = 1
while n1 < 10:
    for m1 in range(1, 10):
        print("%d * %d = %2d" % (n1, m1 , n1*m1), end="  ")
    print("")
    n1 += 1

# continue
n2 = 0
while n2 < 10:
    n2 += 1
    print(n2)
    continue

# break
n3 = 12
while n3 < 8:
    n3 -= 2
    print(n3)
    break

# 演示登录密码3次错误，禁止再次输入
pwd_list = ['*#*#', '123456']

def account_login():
    tries = 3
    while tries > 0:
        pwd = input('password:')
        pwd_right = pwd == pwd_list[-1]
        pwd_reset = pwd == pwd_list[0]
        if pwd_right:
            print('Login Success!')
        elif pwd_reset:
            new_pwd = input("Enter a new password:")
            pwd_list.append(new_pwd)
            print("Password has changed successfully!")
            account_login()
        else:
            print("wrong password or invalid input!")
            tries = tries-1
            print(tries, 'times left')
    else:
        print("Your account has been suspenged'")

if __name__ == "__main__":
    account_login()



