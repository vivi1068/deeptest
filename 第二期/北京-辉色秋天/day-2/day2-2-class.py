#-*-coding:utf-8-*-

class Base1():
    xx = 11#类变量
    
    def __init__(self, y):
       self.y = y#实例变量

    def print_ss(self):
        print("this is Base1   y is %d"%self.y)



class Base2(Base1):
    def __init__(self,y):
        super(Base2, self).__init__(y)
        #Base1.__init__(self,y)

class Base3(Base1):
   def __init__(self, y):
       Base1.__init__(self, y) 

   #函数重写
   def print_ss(self):
        print("this is Base3 y is %d"%self.y)
if __name__ == "__main__":

    ss = Base2(2)

    ss.print_ss()
        
    dd = Base3(3)
    dd.print_ss()
