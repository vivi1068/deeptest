#--coding:utf-8--
import random

class Mysort:

    def __init__(self,start,end,count):
        #stat end为随机数生成范围
       
        self.start=start
        self.end=end
        self.count=count
        
    #用冒泡实现排序
    def __mysort__(self):
        #生成一个随机数列表
        L_random=random.sample(range(self.start,self.end),self.count)
        L_len=len(L_random)
        #对列表进行排序
        for i in range(L_len):
            for j in range(L_len-i-1):
                if L_random[j]>L_random[j+1]:
                    exc=L_random[j]
                    L_random[j]=L_random[j+1]
                    L_random[j+1]=exc

        return L_random

if __name__=="__main__":
    sorted_data=Mysort(10,1000,100)

    #打印排序后的结果
    print(sorted_data.__mysort__())
    
