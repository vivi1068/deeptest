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


#发送读写请求
class SendRequest(object):
    def __init__(self,fileName,udpSocket,ip,requestNum):
        self.fileName=fileName
        self.udpSocket=udpSocket
        self.ip=ip
        self.requestNum=requestNum

    def sengRequest(self):
        # 构造请求数据
        file_request = "!H" + str(len(self.fileName)) + "s" + "b" + "5s" + "b"
    # 下载请求
        cmd_buf = struct.pack(file_request, self.requestNum, self.fileName.encode('UTF-8'), 0, "octet".encode('UTF-8'), 0)
        sendAddr = (self.ip, 69)
        self.udpSocket.sendto(cmd_buf, sendAddr)

#下载
class Fileload(SendRequest):
    def fileDownload(self):
        p_num = 0  # 记录下载次数
        recvFile = ''
        while True:
            # 从服务器接收响应
            recvData, recvAddr = self.udpSocket.recvfrom(516)
            # 接收内容大小
            recvDataLen = len(recvData)
            # 解析接收内容 操作码 块编码
            cmd, currentPackNum = struct.unpack("!HH", recvData[:4])
            if cmd == 3:  # 是否为数据包
                # 如果是第⼀次接收到数据， 那么就创建文件
                if currentPackNum == 1:
                    recvFile = open(self.fileName.encode("utf-8"), "a")
                # 包编号是否和上次相等
                if p_num + 1 == currentPackNum:
                    recvFile.write(str(recvData[4:]))
                    p_num += 1
                    print('(%d)次接收到的数据' % (p_num))
                    # 发送ACK应答包到服务器
                    ackBuf = struct.pack("!HH", 4, p_num)
                    self.udpSocket.sendto(ackBuf, recvAddr)
                # 如果收到的数据⼩于516则认为出错
                if recvDataLen < 516:
                    recvFile.close()
                    print('已经成功下载！ ！ ！ ')
                    break
            elif cmd == 5:  # 是否为错误应答
                print("error num:%d" % currentPackNum)
                break



#上传
class FileUpload(SendRequest):
    def fileUpload(self):
        # 要上传的文件
        ready_to_upload_file = open(self.fileName.encode("utf-8"), "rb+")
        # 起始的快编号标记
        kuaiBiaoHaoFlag = 0
        while True:
            recv_data, recv_adr = self.udpSocket.recvfrom(516)
            print(recv_data)
            caozuoma, kuaibianhao = struct.unpack("!HH", recv_data[:4])
            if (caozuoma == 4):
                if (kuaibianhao == kuaiBiaoHaoFlag):
                    print("服务端已经收到了我的数据，准备上传下一个")
                    # 开始上传数据,此时要像服务端发送数据包，数据大小最大为512
                    kuaiBiaoHaoFlag += 1
                    data = ready_to_upload_file.read(512)
                    print(data)
                    if (data == ("".encode("utf-8"))):
                        print("上传结束")
                        break
                    '''if (kuaibianhao == 65535):
                        kuaiBiaoHaoFlag = 0
                        kuaibianhao = 0'''
                        # 数据包
                    data_request = "!H" + "H" + str(len(data)) + "s"
                    shujuBao = struct.pack(data_request, 3, kuaiBiaoHaoFlag, data)
                    self.udpSocket.sendto(shujuBao, recv_adr)
                else:
                    print("服务端没收到我上传的数据")
                    break

        ready_to_upload_file.close()



def main():
    # 创建udp套接字
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    #输入相关信息
    ip = input('>>请输入目标ip：')
    print('输入1下载文件，输入2上传文件')
    requestNum =int(input('>>请输入选择'))
    if requestNum == 1:
        fileName = input('>>请输入需要下载的文件名：')
        # 发送下载请求
        File_load = Fileload(fileName,udpSocket,ip,requestNum)
        File_load.sengRequest()
        File_load.fileDownload()
    else:
        fileName = input('>>请输入需要上传的文件名：')
        # 发送上传请求
        File_load = FileUpload(fileName,udpSocket,ip,requestNum)
        File_load.sengRequest()
        File_load.fileUpload()
    #关闭连接
    udpSocket.close()

if __name__=='__main__':
    main()