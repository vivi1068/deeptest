import random
class MySort():
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.numlist= []       

    #随机生成数据，并加入到列表中
    def __generate__(self):
        for i in range(self.count):
            self.numlist.append(random.randint(self.start, self.end))
    #交换排序
    def mysort(self):
        self.__generate__()
        for i in range(self.count-1):
            for j in range(i+1, self.count):
                if self.numlist[i] > self.numlist[j]:
                    self.numlist[i], self.numlist[j] = self.numlist[j], self.numlist[i]
    #输出数据    
    def printdata(self):
        for i in range(self.count):
            print(self.numlist[i])


if __name__ == "__main__":
    sorted_data = MySort(10, 1000, 100)

    sorted_data.mysort()
    sorted_data.printdata()
