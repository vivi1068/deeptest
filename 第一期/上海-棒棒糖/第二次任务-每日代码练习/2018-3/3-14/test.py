from socket import *
#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
#2. 准备接收⽅的地址
sendAddr = ('10.224.67.10', 8080)
#3. 从键盘获取数据
#sendData = str(input("请输入要发送的数据:"))
#4. 发送数据到指定的电脑上
udpSocket.sendto(b'798798485', sendAddr)
#5. 关闭套接字
udpSocket.close()



