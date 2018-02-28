#实现一个四则运算的类，要求实现任意两个数的加减乘除运算

class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        try:
            if self.b == 0 :
                print("除数不能为0")
        except ValueError:
            print("除数不能为0")
        return self.a // self.b

def calc_sum(calc):
    sum =  calc.add()
    print("a+b=%d" % sum)

def calc_sub(calc):
    sub =  calc.sub()
    print("a-b=%d" % sub)

def calc_mul(calc):
    mul =  calc.mul()
    print("axb=%d" % mul)

def calc_div(calc):
    div =  calc.div()
    print("a÷b=%d" % div)


if __name__ == "__main__":
    a = int(input("输入a:"))
    b = int(input("输入b:"))
    select = input("请选择加减乘除:")
    calc = Calc(a,b)
    if select == "加":
        calc_sum(calc)
    elif select == "减":
        calc_sub(calc)
    elif select == "乘":
        calc_mul(calc)
    elif select == "除":
        calc_div(calc)
    else:
        print('只能输入加减乘除，输入错误无法计算结果！')


