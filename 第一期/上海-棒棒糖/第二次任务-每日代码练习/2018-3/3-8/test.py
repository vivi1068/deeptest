from types import MethodType

class Student(object):
    def __init__(self,age):  # 定义一个函数作为实例方法
        self.age=age

def old(self):
    print('年纪是%s'%self.age)

@classmethod
def set_score(cls, score):
    cls.score = score
    print(cls.score)


s = Student(20)
s1=Student(30)
#Student.set_score = MethodType(set_score, Student)  # 给实例绑定一个方法
Student.set_score=set_score
s.set_score(50)  # 调用实例方法
s1.set_score(60)



