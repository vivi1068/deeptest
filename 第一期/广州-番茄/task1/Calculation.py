class Calc:
    # 初始化
    def __init__(self,a,b):
        self.a =int(input("请输入第一个数字: "))
        self.b =int(input("请输入第二个数字: "))
        if self.b==0:
            print("第二个数字不能为0")
            self.b =int(input("请输入第二个数字: "))
        else:
            self.b=b
    # 加法
    def __add__(self):
        print("加法结果是:",end="")
        return self.a+self.b
    # 减法
    def __sub__(self):
        print("减法结果是:",end="")
        return self.a-self.b
    # 乘法
    def __mul__(self):
        print("乘法结果是:",end="")
        return self.a*self.b
    # 除法
    def __div__(self):
        print("除法结果是:",end="")
        return self.a/self.b
     
Calc_obj=Calc(6,8)
print(Calc_obj.__add__())
print(Calc_obj.__sub__())
print(Calc_obj.__mul__())
print(Calc_obj.__div__())



