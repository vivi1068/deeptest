class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def __add__(self):
        s = self.a + self.b
        print(s)
        return s

    # 减法
    def __sub__(self):
        sub = self.a - self.b
        print(sub)
        return sub

    # 乘法
    def mul(self):
        mul = self.a * self.b
        print(mul)
        return mul

    # 除法
    def div(self):
        if self.b == 0:
            print("除数不能为0")
            exit(1)
        else:
            div = float(self.a) / self.b
            print(div)
            return div


if __name__ == "__main__":
      compute = Calc(3.0, 5.2)
      compute.__add__()
      compute.__sub__()
      compute.mul()
      compute.div()

