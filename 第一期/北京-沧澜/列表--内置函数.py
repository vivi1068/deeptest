#_*_coding:utf-8_*_
if __name__ == "__main__":
    list_demo = [1,2,3,4,5,6,7,8,9]
    print('list内置函数处理示例')
    #计算list_demo中元素个数
    print(len(list_demo))
    #返回list_demo中的最小值
    print(min(list_demo))
    #返回list_demo中的最大值
    print(max(list_demo))
    #将元组转换成列表
    tuple_demo = (1,2,3,4,5)
    list1 = list(tuple_demo)
    print(list1)