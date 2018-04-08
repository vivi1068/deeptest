from threading import Thread
from socket import *
#发送数据
def sendData():
    while True:
        sendInfo = input('<<')
        udpSocket.sendto(sendInfo.encode('gb2312'),(destIp,destPort))
#接收数据
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print('\r<<%s:%s\n<<'%(str(recvInfo[1]),recvInfo[0].decode('gb2312')))

#给变量默认值，参数是对象用None，str用''，int用0
udpSocket = None
destIp = ''
destPort = 0


#主函数控制流程
def main():
    global udpSocket
    global destIp
    global destPort

    destIp = input('对方的ip:')
    destPort = int(input('对方的port:'))

    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(('',4570))

    #创建线程
    ts=Thread(target=sendData)
    tr = Thread(target=recvData)

    #执行线程
    ts.start()
    tr.start()
    ts.join()
    tr.join()

if __name__ == '__main__':
    main()