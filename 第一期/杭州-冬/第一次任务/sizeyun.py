#--coding:utf-8--
class Calc:
    #
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #加法 用%d替换变量
    def __add__(self):
        print("%d + %d= %d" %(self.a,self.b,self.a+self.b))

    #减法 用%d把任何数据类型转化为字符串
    def __sub__(self):
        print("%s - %s= %s" %(self.a,self.b,self.a-self.b))

    #乘法
    def mul(self):
        print("%d * %d= %d" %(self.a,self.b,self.a*self.b))

    #除法
    def div(self):
        print("%d / %d= %d" %(self.a,self.b,self.a/self.b))
if __name__=="__main__":
    calc_obj=Calc(2,3)
    calc_obj.__add__()
    calc_obj.__sub__()
    calc_obj.mul()
    calc_obj.div()
    
