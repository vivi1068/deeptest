from socket import *
def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAddr = ('', 7790)
    udpSocket.bind(bindAddr)
    num = 1
    while True:
        recvData = udpSocket.recvfrom(1024)
        #将接收到的数据再发送给对⽅
        udpSocket.sendto(recvData[0],recvData[1])
        # 统计信息
        print('已经将接收到的第%d个数据返回给对方,内容为:%s'%(num, recvData[0].decode('gb2312')))
        num+= 1

if __name__ == '__main__':
    main()
