import random

class MySort:
    def __init__(self,start,end,count):
        self.start =start
        self.end =end
        self.count =count
        self.random_data = []

    #生成随机整数
    def __generator(self):
        for i in range(0,self.count):
            self.random_data.append(random.randint(self.start,self.end))

    #实现排序
    def sort(self):
        self.__generator()
        n = len(self.random_data)
        for i in range(0,n):
            for j in range(1,n-i):
                if self.random_data[j-1]>self.random_data[j]:
                    self.random_data[j-1],self.random_data[j]=self.random_data[j],self.random_data[j-1]
        return self.random_data

if __name__ =="__main__":
    sorted_data =MySort(10,1000,10)
    data=sorted_data.sort()
    for d in data:
        print(d)

