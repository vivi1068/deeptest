# coding=utf-8
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
        if self.b != 0:
            return self.a/self.b
        else:
            print("被除数为0不能操作")

    def reset(self, a, b):
        self.a = a
        self.b = b
