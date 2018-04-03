from socket import *
import struct
import sys
'''
if len(sys.argv) != 2:
    print('-'*30)
    print("tips:")
    print("python xxxx.py 192.168.1.1")
    print('-'*30)
    exit()
else:
    ip = sys.argv[0]'''
ip = input('>>请输入目标ip：')
fileName = input('>>请输入需要下载的文件名：')
#print(len(fileName))
#print(str(len(fileName)) + "s")

# 创建udp套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#构造下载请求数据
file_down_load_request = "!H" + str(len(fileName)) + "s" + "b" + "5s" + "b"
#print(file_down_load_request)
cmd_buf = struct.pack(file_down_load_request,1,fileName.encode('UTF-8'),0,"octet".encode('UTF-8'),0)

#发送下载文件请求数据到指定服务器
sendAddr = (ip, 69)
udpSocket.sendto(cmd_buf, sendAddr)

p_num = 0 #记录下载次数
recvFile = ''
while True:
    #从服务器接收响应
    recvData,recvAddr = udpSocket.recvfrom(516)
    #接收内容大小
    recvDataLen = len(recvData)
    #解析接收内容 操作码 块编码
    cmd,currentPackNum = struct.unpack("!HH", recvData[:4])
    if cmd == 3: #是否为数据包
    # 如果是第⼀次接收到数据， 那么就创建文件
        if currentPackNum == 1:
            recvFile = open(fileName, "a")
        # 包编号是否和上次相等
        if p_num+1 == currentPackNum:
            recvFile.write(str(recvData[4:]))
            p_num +=1
            print('(%d)次接收到的数据'%(p_num))
            #发送ACK应答包到服务器
            ackBuf = struct.pack("!HH",4,p_num)
            udpSocket.sendto(ackBuf, recvAddr)
    # 如果收到的数据⼩于516则认为出错
        if recvDataLen<516:
            recvFile.close()
            print( '已经成功下载！ ！ ！ ')
            break
    elif cmd == 5: #是否为错误应答
        print("error num:%d"%currentPackNum)
        break
udpSocket.close()