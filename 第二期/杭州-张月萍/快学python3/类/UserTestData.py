# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import random


# 制作一个填充用户数据的小工具
ln_path = 'C:/Users/Carina/Desktop/last_name.txt'
fn_path = 'C:/Users/Carina/Desktop/first_name.txt'
fn = []
ln1 = []        #单字名
ln2 = []        #双字名

with open(fn_path,'r') as f:
    # print(f.readline())
    for line in f.readline():
        fn.append(line.split('\n')[0])
print(fn)

with open(ln_path ,'r') as f:
    for line in f.readline():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split(',')[0])
        else:
            ln2.append(line.split(',')[0])
print(ln1)
print('='*70)     #分割线
print(ln2)

# 定义父类,Fakeuser功能：随机姓名和性别
class FakeUser():
    def fake_name(self,amount=1,one_word=False,two_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            print(full_name)
            #yield 的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
            yield full_name
            n += 1

    def fake_gender(self,amount=1):
        n=0
        while n <=amount:
            gender = random.choice (['男','女','未知'])
            print(gender)
            yield gender
            n += 1

# 定义子类，SnsUser功能：随机数量的跟随者
class SnsUser(FakeUser):
    def get_followers(self,amount=1,few=True,a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1,50)
            elif a_lot:
                followers = random.randrange (200,10000)
            yield followers
            n += 1

user_a = FakeUser()
user_b = SnsUser()

for name in user_a.fake_name(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)