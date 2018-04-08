class Calc(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sub(self):
        return (self.a - self.b)

    def add(self):
        return (self.a + self.b)

    def mul(self):
        return (self.a*self.b)

    def div(self):
        return (self.a/self.b)


def main():
    formula = input("Please input your Computational formula with blank space (like '5 * 11'):\n")
    num_list = formula.split(" ")
    cal = Calc(float(num_list[0]), float(num_list[2]))
    if num_list[1] == "+":
        print(cal.add())
    elif num_list[1] == "-":
        print(cal.sub())
    elif num_list[1] == "*":
        print(cal.mul())
    elif num_list[1] == "/":
        print(cal.div())

main()
