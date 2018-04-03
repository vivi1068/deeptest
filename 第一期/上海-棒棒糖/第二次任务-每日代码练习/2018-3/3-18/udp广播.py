#coding=utf-8
import socket, sys
#发送广播ip使用<broadcast>
dest = ('<broadcast>', 7788)
# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对这个需要发送⼴播数据的套接字进⾏修改设置， 否则不能发送⼴播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
# 以⼴播的形式发送数据到本⽹络的所有电脑中
s.sendto("Hi", dest)
print("等待对⽅回复（按ctrl+c退出） ")
while True:
    (buf, address) = s.recvfrom(2048)
    print("Received from %s: %s" % (address, buf))