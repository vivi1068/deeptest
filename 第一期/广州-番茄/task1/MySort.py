#conding=utf-8

import random
class MySort:
    #初始化
    def __init__(self,start,end,count):
        self.start=start
        self.end=end
        self.count=count
        
    def mysort(self):
        #对参数的数据类型做检查
        if not isinstance(self.start,(int))&isinstance(self.end,(int))&isinstance(self.count,(int,float)):
            raise TypeError('参数必须是整数')
        #生成随机数列表
        temp=[]
        for i in range(self.count):
            ran_data=random.randint(self.start,self.end)
            temp.append(ran_data)
        #从小到大排序列表
        for i in range(self.count):
            for j in range(i):
                if temp[j]>temp[j+1]:
                    temp[j],temp[j+1]=temp[j+1],temp[j]
        return temp                    
        
#使用示例
if __name__ == '__main__':
    sorted_Data = MySort(10,1000,100).mysort()
    #打印排序后的结果
    print(sorted_Data)



