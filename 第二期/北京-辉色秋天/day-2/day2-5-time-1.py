
import time

if __name__ == "__main__":

    localtime = time.asctime(time.localtime())
    print("corrent time is %s",localtime)

    print("24小时制",time.strftime('%Y-%m-%d %H:%M:%S %A', time.localtime()))

    print("12小时制",time.strftime('%Y-%m-%d %I:%D:%S %a', time.localtime()))

    print("带a.m或p.m 24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime() ))
    print("带时区的全格式：", 
        time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))
    
    print("随意排格式：", 
        time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))


