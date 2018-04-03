#-*-coding-*-

if __name__ == "__main__":
    for i in [1,23,45,6,6]:
        print(i)

    for i in range(10):#前闭后开
        print(i)

    for i in range(1,10):
        for j in range(1,i+1):
            print("%d * %d = %2d"%(j, i, i*j),end='    ')
        print()



    n = 1
    while(n < 10):
        for x in range(1, n+1):
            print("%d * %d = %2d"%(x, n, x*n),end='    ')
        print()
        n += 1

    print("请输入任意序列，如果是偶数，则除以2，基数直接输出,输入exit输出处理后列表")
    list1 = []
    
    while(True):
        ss = input()
        if ss.isdigit():
            ssint = int(ss)
            if ssint%2 == 0:
                ssint /= 2 
                list1.append(int(ssint))
            else:
                list1.append(ssint)
                continue
        elif ss == 'exit':
            print("exit")
            break;
        else:
            print("输入非数字字符，自动忽略")
 
   
    print("输出列表")
    for i in list1:
        print(i)
