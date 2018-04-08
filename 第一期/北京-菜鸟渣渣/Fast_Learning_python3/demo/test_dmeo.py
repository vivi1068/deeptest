# # 定制类
#
# 1) __str__
# 我这么麻烦就是为了打扮一下更好看, 好看的都展示给用户，不好看的丢给程序员们吧，给加个__repr__ = __str__
# eg:
#
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         print('Student object (name: %s) % self.name')
#
#     __repr__ = __str__
#
#
# print(Student('VV'))
#
# # 打印结果：
# Student
# object(name: VV)
#
# 2) __iter__
# 返回一个迭代对象，与__next__拿到循环的下一个值结合起来实现实例请参考文档‘定制裴波那契三种类’
#
# 3) __getitem__
# 像list一样可以取回list中的元素
#
# 4) __getattr__
# 动态返回属性
# eg:
#
#
# class Student(object):
#     def __init__(self):
#         self.name = 'VV'
#
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 404
#
#
# s = Student()
# print(s.name)
# print(s.score)
#
# 5) __call__
# 可以直接对实例进行调用
# eg:
#
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
#
# s = Student('VV')
# s()
#
# # 执行结果为
# My
# name is VV
#
# ###使用枚举类
# Enum(cls, value) ：用这个类来实现每个常量都是class的一个唯一实例
# eg:

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)

# # 执行结果：
# Jan == > Month.Jan, 1
# Feb == > Month.Feb, 2
# Mar == > Month.Mar, 3
# Apr == > Month.Apr, 4
# May == > Month.May, 5
# Jun == > Month.Jun, 6
# Jul == > Month.Jul, 7
# Aug == > Month.Aug, 8
# Sep == > Month.Sep, 9
# Oct == > Month.Oct, 10
# Nov == > Month.Nov, 11
# Dec == > Month.Dec, 12
#
# 1)定义枚举时，成员名称不允许重复；
# 2)默认情况下，不同的成员值允许相同，但是两个相同值的成员，第二个的名称会被视作为第一个成员的别名；
# 3)如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
# 4)如果要限制定义枚举时，不能定义相同值的成员，可以使用装饰器 @ unique(需要导入unique模块)
# eg:
# from enum import Enum, unique
#
#
'''
@unique
class Weekday(Enum):  # 枚举定义用class关键字，继承Enum类

    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon.value
print(day1)
print(Weekday.Mon)
print(Weekday)
#
# ###使用元类
# pass（不懂）


'''

