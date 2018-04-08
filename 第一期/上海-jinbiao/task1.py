class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return round(self.a / self.b,2)


if __name__ == "__main__":
    one = int(input("请输入第一个数字"))
    two = int(input("请输入第二个数字"))
    op = str(input("请输入你的运算符"))
    mid = Calc(one,two)
    if op == "+":
        result=Calc.add(mid)
    elif op == "-":
        result=Calc.sub(mid)
    elif op == "*":
        result=Calc.mul(mid)
    else:
        result=Calc.div(mid)
    print(result)
