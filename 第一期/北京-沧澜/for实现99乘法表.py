# _*_coding:utf-8_*_
if __name__ == "__main__":
    print('两个range实现9*9乘法表')
    for i in range(1, 10):
       for j in range(i, 10):
           print(u"%d * %d = %2d" % (i, j,i * j), end = "  ")

       print("")
