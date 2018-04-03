from socket import *
def main():
    # 1. 创建套接字
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    # 2. 绑定本地的相关信息， 如果一个网络程序不绑定， 则系统会随机分配
    bindAddr = ('', 7788)  # ip地址和端⼝号， ip一般不用写， 表示本机的任何一个ip
    udpSocket.bind(bindAddr)
    # 3. 等待接收对方发送的数据，接收到内容为元组里面有(发送的内容,发送方信息)
    while True:
        recvData = udpSocket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        # recvData是个元组，a,b=(100,200),那么a=100,b=200
        # content,desInfo = recvData
        # 4. 显示接收到的数据
        # print('content is %s'%content.decode('gb2312'))
        print('%s:%s'%(str(recvData[1]), recvData[0].decode('gb2312')))

#5. 关闭套接字
if __name__ == '__main__':
    main()
