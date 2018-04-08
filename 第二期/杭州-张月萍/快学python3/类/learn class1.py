# -*- coding: utf-8 -*-
# __author__ = 'Carina'


# 类的属性
class CocaCola:
    # 配方
    formula = ['caffeine','suger','water','soda']

    # 实例方法，方法就是函数
    def drink(self):  # self其实就是被创建的实例本身
        print('Energy')

    # 更多参数
    def drink1(self, how_much):
        if how_much == 'a ship':
            print('cool~')
        elif how_much == 'whole bottle':
            print('Headache！')

    # 魔术方法 _init_，即使创建实例时不去引用_init_()方法，其中的命令也会先被自动执行
    def __init__(self):
        self.local_logo = '可口可乐'

print(CocaCola.formula)

# 类的实例化（类的属性被所有类的实例共享）
coke_for_me =CocaCola()
coke_for_you =CocaCola()
print(coke_for_me.formula)
print(coke_for_you.formula)

# 输出类的属性值
print("输出类的属性值:", end= ' ')
for element in CocaCola.formula:
    print(element, end= ' ')
print('\n')

# 类实例化
coke = CocaCola()
coke.drink()   # 等同于CocaCola.drink(coke)

ice_coke = CocaCola()
ice_coke.drink1('a ship')

# 输出类的属性
coke = CocaCola()
print(coke.local_logo)
