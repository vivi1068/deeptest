class People(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self): #获取
        return self.__name

    @name.setter
    def name(self, newName): #设置
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error:名字长度需要大于或者等于5")

xiaoming = People("dongGe")
xiaoming.name='wanger'
print(xiaoming.name)




