def test(number):
    print('--1--')
    def test_in(number2):
        print('--2--')
        print(number+number2)
    print('--3--')
    return test_in

ret=test(100)#因为有return test_in，test(100)指向test_in的引用，所有变量ret相当于是test_in，可以直接调用
ret(200)

#应用
def test(a,b):
    def test_in(x):
        print(a*x+b)
    return test_in
line1=test(1,1)#相当于y=1*x+1
line1(0)
line2=test(10,4)#相当于y=10*x+4
line2(5)