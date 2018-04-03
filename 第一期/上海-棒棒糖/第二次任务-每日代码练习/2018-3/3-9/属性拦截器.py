class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    #属性访问时拦截器， 打log
    def __getattribute__(self,obj):
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            return object.__getattribute__(self,obj)

    def show(self): #类中的方法实际是在这个类空间外创建好后，用变量show指向
        print('this is Itcast')

s = Itcast("python")
print(s.subject1) #访问属性，自动调用__getattribute__方法
print(s.subject2)
s.show()  #先调用__getattribute__方法，执行到else后调用父类的__getattribute__返回show的引用


class Person(object):
    def __getattribute__(self,obj):
        print("---test---")
        if obj.startswith("a"):
            return "hahha"
        else:
            return self.test
    def test(self):
        print("heihei")

t=Person()
t.a #返回hahha
t.b #返回self.test后依旧调用__getattribute__，不选循环，内存溢出