 #随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
import random

class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end,count):
        self.start = start
        self.end = end
        self.count = count
        self.random_data = []

    # 生成随机列表
    def generator(self):
        for i in range(0,self.count):
            self.random_data.append(random.randint(self.start,self.end))
        return self.random_data

    # 实现排序，内部函数
    def mysort(self):
        self.generator()
        for i in range(0,len(self.random_data)):
            for j in range(1,len(self.random_data)-1):
                if self.random_data[j-1] > self.random_data[i]:
                    self.random_data[j-1],self.random_data[i] = self.random_data[i],self.random_data[j-1]
        return self.random_data


# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10,100,20)
    data = sorted_data.mysort()
    print(data)

    # 打印排序后的结果

