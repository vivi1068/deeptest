class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print('--%s正在吃东西--'%self.name)



#定义lei ⽅法
@classmethod
def run(cls):
    print('--%s正在跑步--')

Person.run=run

p=Person('小米',20)
p.run()



#给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()  # 创建新的实例
s2.set_age(25)  # 尝试调用方法

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

 Student.set_score = MethodType(set_score, Student)
#给class绑定方法后，所有实例均可调用：
s.set_score(100)
s.score
s2.set_score(99)
s2.score


