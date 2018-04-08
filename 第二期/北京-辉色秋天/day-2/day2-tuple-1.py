#-*-coding:utf-8-*-

if __name__ == "__main__":

    tuple_d = (1,2,3,56,4,78,95,5,2,2,12)

    print(tuple_d)
    print("len(tuple_d) is%d"%(len(tuple_d)))

    print("返回tuple_d中最大值"+str(max(tuple_d)))
    print("返回tuple_d中最小值"+str(min(tuple_d)))

    print("转换成列list")
    list1 = [1,8,9,10]
    print(tuple(list1))


    ''' 切片'''

    tuple_d = (1,2,3,4,5,6)

    print("间隔一项输出")
    print(tuple_d[::2])

    print("倒叙输出")
    print(tuple_d[::-1])
    print(tuple_d[-1::-1])

    '''合并'''

    tuple1 = (1,2,3,4,5)
    tuple2 = (',','上','山','打','老','虎')
  
    tuple3= tuple1 + tuple2

    print(tuple3)
    tuple4 = tuple1*2 + tuple2
    print(tuple4)

    print(list(tuple4))
