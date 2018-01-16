#!/usr/bin/python
# coding=utf-8
# Filename: cacl.py
# 2018-01-09

__author__ = "nancy"

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __isNum__(self):
        if (type(self.a) != int) or (type(self.b) != int):
            raise('error:a、b must be int!')

    # add
    def __add__(self):
        self.__isNum__()
        return self.a + self.b

    # sub
    def __sub__(self):
        self.__isNum__()
        return self.a - self.b

    # mul
    def __mul__(self):
        self.__isNum__()
        return self.a * self.b

    # div
    def __div__(self):
        self.__isNum__()
        if self.b != 0:
            # 0.00
            return round(self.a / self.b, 2)
        print('error:divisor cannot be 0!')   #raise

def testcalc(calc):
    print('--a:'+str(calc.a),'b:'+str(calc.b))
    addn = calc.__add__()
    sub = calc.__sub__()
    mul = calc.__mul__()
    div = calc.__div__()
    print(addn, sub, mul, div)

if __name__ == "__main__":
    # test
    calc1 = Calc(3, 6)
    testcalc(calc1)
    calc2 = Calc(2, -2)
    testcalc(calc2)
    calc2 = Calc(-5, -3)
    testcalc(calc2)
    calc4 = Calc(112312312312311224323424121212121212, 1121223123123123123123123123123123)
    testcalc(calc4)
    calc5 = Calc(2, 0)
    testcalc(calc5)
    calc6 = Calc(2.5, 6.1)
    testcalc(calc6)
    calc7 = Calc('ASD', 123123123123123123123123123123)
    testcalc(calc7)


