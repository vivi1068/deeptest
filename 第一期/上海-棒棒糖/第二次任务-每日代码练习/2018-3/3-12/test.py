
class Fjs(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("said by : ", self.name)

    def show(self): #类中的方法实际是在这个类空间外创建好后，用变量show指向
        print('this is Itcast %s'%self.name )

    def __getattribute__(self, item):
        print("访问了特性：" + item)
        return object.__getattribute__(self, item)


fjs = Fjs("fjs")
#print(fjs.name)
fjs.hello()
fjs.show()