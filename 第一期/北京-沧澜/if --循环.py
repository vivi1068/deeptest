#_*_coding:utf-8_*_
if __name__ == "__main__":
    var1 = int(input('请输入一个整数'))
    if var1 >0 and var1<10:
        print('你输入了一个大于0小于10的整数')
    elif var1>=10:
        print('你输入了一个大于等于10的整数')
    else:
        print('你输入了一个负数')