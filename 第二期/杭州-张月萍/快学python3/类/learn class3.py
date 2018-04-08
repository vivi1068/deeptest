# -*- coding: utf-8 -*-
# __author__ = 'Carina'


class CocaCola:
    calories = 140
    sodium =45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

# 类的继承,CaffeineFree继承了CocaCola
class CaffeineFree(CocaCola):
    caffeine = 0  # 覆盖
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]

coke_a = CaffeineFree('Cocacola-Free')
coke_a.drink()