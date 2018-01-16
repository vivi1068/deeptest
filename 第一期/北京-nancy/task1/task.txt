第一次任务

基本要求
注册一个云笔记，用于记录每天的任务和记录每天学习心得
每天分享学习心得到专用群里，以供大家相互监督（最好每天早上9点30前分享到群里）
初级篇
安装PyCharm社区版，并完成第一个Python程序
安装Visual Studio Code，配置Python开发环境，并完成第一个Python程序
安装JupyterLab，并完成第一个Python程序
上述三个任务可任一选择一个你喜欢的，进行完成，我推荐： 2 和 3

阅读篇
阅读Python3官方手册，掌握Python3常用标准库功能分类，并了解每个分类的作用
找一本python入门书籍，掌握以下语法结构，要求做到不看书也能清楚的掌握：
a. if语法
b. for语法
c. 函数定义、传参以及返回值
d. 类的定义
请购买一本Python学习书籍，推荐《Python基础教程》，如果你已经有了一本python学习的书籍，则不需要购买，如要购买，请买《Python核心编程》最新版，等深入的时候要用到，或以后作为手册时常翻阅
代码篇
实现一个四则运算的类，要求实现任意两个数的加减乘除运算
class Calc:
    # 初始化
    def __init__(self, a, b):
        pass

    # 加法
    def __add__(self):
        pass

    # 减法
    def __sub__(self):
        pass

    # 乘法
    def mul(self):
        pass

    # 除法
    def div(self):
        pass


随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end，count):
        pass

    # 实现排序，内部函数
    def __mysort__(selg):
        pass

# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10， 1000， 100)

    # 打印排序后的结果
    print(sorted_data)