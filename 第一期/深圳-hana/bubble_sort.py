#-*-coding:utf-8-*-
#随机生成100个10至1000之间的数，对生成的100个数进行排序，
# 禁止使用Python自带的排序函数，要自己实现排序函数
import random
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # totalNum为生成的随机数个数
    def __init__(self, start, end,totalNum):
        self.start = start
        self.end = end
        self.totalNum = totalNum


    # 实现排序，内部函数
    def sortNums(self):
        Nums= []
        num = 1
        numLen = self.totalNum
        startNum  = self.start
        endMum = self.end
        while num<numLen+1:
            Nums.append(random.randint(startNum,endMum))
            num+=1
         print("排序前："+str(Nums))
        totalNum = len(Nums)
        for i in range(0, totalNum):
            for j in range(i + 1, totalNum):
                if Nums[i] > Nums[j]:
                    Nums[i], Nums[j] = Nums[j], Nums[i]
        print("排序后："+str(Nums))
        return Nums

# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10,1000,100)
    # 打印排序后的结果
    print(str(sorted_data.sortNums()))
