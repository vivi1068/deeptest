#-*-coding:utf-8-*-
'''必选参数，默认参数，可变参数，关键字参数'''
def test1(x, y = 10, *number, **kw):
    print("x="+str(x))
    print("y="+str(y))
    print("num="+str(number))
    print("kw="+str(kw))


'''必选参数，默认参数，可变参数，命名关键字参数 python2 会报错'''
def test2(x, y = 10, *number, p):
    print("x="+str(x))
    print("y="+str(y))
    print("num="+str(number))
    print("p="+str(p))
    #print("p2="+str(p2))


'''必选参数，默认参数，命名关键字参数 规则，命名关键字参数之前没有可变参数，必须添加* '''
def test3(x, y = 10, *, p):
    print("x="+str(x))
    print("y="+str(y))
    print("p="+str(p))



'''必选参数，默认参数 '''
def test4(x, y = 10):
    print("x="+str(x))
    print("y="+str(y))

def test5(dd):
    dd.append('xx')
    return True
if __name__ == "__main__":
    test1(1,2,3,city="222")
    test1(1,2,34,4,5,54,4,4,city="222o")

    test2(1,2,3,4,p=1)
    
    test3(1,2,p=12)
    test4(1)
    list2=[1,2,3,6]
    test5(list2)
    print(list2)
