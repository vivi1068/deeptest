'''
类名：Calculate
功能：可自动生成两个参数，计算加减乘除，也可手动输入参数，可以判定用户输入数据是否合理
开发环境：python3

'''
import random
class Calculate():

    def __init__(self, a, b):
        self.a = a 
        self.b = b
    
    def __add__(self):
        return (self.a + self.b)

    def __sub__(self):
        return (self.a - self.b)
 
    def __mul__(self):
        return (self.a * self.b)
   
    def __div__(self):
        return (self.a / self.b)

  
    def cal(self):
        print("the result of '+' is %f"%(self.__add__()))
        print("the result of '-' is %f"%(self.__sub__()))
        print("the result of '*' is %f"%(self.__mul__()))
        print("the result of '/' is %f"%(self.__div__()))

def Isfloat(a):
    try:
        f = float(a)
        return f
    except ValueError:
        return False

if __name__ == "__main__":
    while True:
        print("自动生成数据 输入 a ")
        print("手动输入数据 输入 h ")
        print("退出 输入 e ")
        x = input("请输入:")
        if "e" == x:
            print("程序退出")
            break

        elif "a" == x:
            a = random.random()
            b = random.random()
            print("生成数据为 a=%f, b=%f"%(a,b))
        elif 'h' == x:
            a = input("请输入 a:")
            b = input("请输入 b:")
            a = Isfloat(a)
            b = Isfloat(b)
            if a is False or b is False:
                print("输入信息不可计算\n\n")
                continue
        else:
            print("输入有误\n\n") 
            continue
 
        calculate = Calculate(a, b)
        calculate.cal()
        print("\n\n")
