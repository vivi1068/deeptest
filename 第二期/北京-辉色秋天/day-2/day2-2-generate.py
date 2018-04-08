#-*-coding:utf-8-*-
'''
def yanghui(n,listall):
    listt=[]
    if n <= 1 :
        listall.extend([[1]])
    else:
        listall.extend([[1],[1,1]])

    for i in range(2, n):
        listt = []
        listt.append(1)
        for j in range(1,i):
            t = listall[i-1][j] + listall[i-1][j-1]
            listt.append(t)
        listt.append(1)

        listall.append(listt)


if __name__ == "__main__":
    listall=[]
    n = int(input('请输入n的值，决定打印层数：'))
    yanghui(n, listall)
    print(listall)
        
  '''

def yanghui():
    list_befor=[1] 

    while True:
        yield list_befor
        list_now=[]
        list_now.append(1)
        for i in range(1,len(list_befor)):
            list_now.append(list_befor[i]+list_befor[i-1])
        list_now.append(1)
        list_befor = list_now

'''
列表生成式，很高级简单的算法
'''
def yanghui2():
    L=[1]
    while True:
        yield L
        L = [1] + [L[n-1]+L[n] for n in range(1,len(L))] + [1]

if __name__ == "__main__":
    ss = yanghui2()

    for i in range(6):
       print(next(ss))
