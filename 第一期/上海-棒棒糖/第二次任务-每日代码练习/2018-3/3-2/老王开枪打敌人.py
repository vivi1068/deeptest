#人类
class Person(object):
    def __init__(self,name):
        super(Person, self).__init__()
        self.name=name
        self.gun=None
        self.hp=100

     # 把子弹装在弹夹里
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    #把弹夹装在枪里
    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        gun_temp.baocun_danjia(dan_jia_temp)
    #拿枪
    def naqiang(self,gun_temp):
        self.gun=gun_temp
    def __str__(self):
        if self.gun:
            return '%s的血量是：%d,他有枪，%s'%(self.name,self.hp,self.gun)
        else:
            return '%s的血量是：%d,他没枪'%(self.name,self.hp)
    #扣扳机
    def kou_ban_ji(self,diren):
        self.gun.fire(diren)
    #子弹打中，会掉血
    def diao_xue(self,sha_shang_li):
        self.hp-=sha_shang_li

#子弹类
class Zidan(object):
    def __init__(self,sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li=sha_shang_li
    #子弹打中敌人，敌人掉血
    def danzhong(self,diren):
        diren.diao_xue(self.sha_shang_li)


#弹夹类
class Danjia(object):
    def __init__(self,max_num):
        super(Danjia, self).__init__()
        #弹夹最大容量
        self.max_num=max_num
        #弹夹保存的子弹
        self.zidan_list = []
     #子弹保存在弹夹里
    def baocun_zidan(self,zidan_temp):
        self.zidan_list.append(zidan_temp)
    def __str__(self):
        return'弹夹的信息为：%d/%d'%(len(self.zidan_list),self.max_num)
    #开枪子弹是先进先出
    def tanchu_zidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None


#枪类
class Gun(object):
    def __init__(self,name):
        super(Gun, self).__init__()
        # 用来记录枪的类型
        self.name = name
        # 用来记录弹夹对象的引用
        self.danjia=None
    #弹夹保存在枪里
    def baocun_danjia(self,dan_jia_temp):
        self.danjia=dan_jia_temp
    def __str__(self):
        if self.danjia:
            return '枪的信息为：%s,%s'%(self.name,self.danjia)
        else:
            return '枪的信息为：%s,没有弹夹'%(self.name)
    #枪从弹夹中获取一发子弹，然后让这发子弹去击中敌人
    def fire(self,diren):
        #弹夹中弹出子弹
        zidan_temp=self.danjia.tanchu_zidan()
        # 子弹打中敌人
        if zidan_temp:
            zidan_temp.danzhong(diren)
        else:
            print('弹夹中没有子弹')




def main ():
    #创建老王
    laowang=Person('老王')
    #创建子弹
    zi_dan=Zidan(10)
    #创建弹夹
    dan_jia=Danjia(20)
    #创建枪
    ak47=Gun('AK47')
    #子弹安装在弹夹中
    laowang.anzhuang_zidan(dan_jia,zi_dan)
    #弹夹安装在枪中
    laowang.anzhuang_danjia(ak47,dan_jia)
    #test:测试弹夹的信息
    print(dan_jia)
    #test:测试枪的信息
    print(ak47)
    #老王拿枪
    laowang.naqiang(ak47)
    #测试老王
    print(laowang)
    #创建敌人
    gebi_laosong=Person('隔壁老宋')
    print(gebi_laosong)
    #用枪打敌人一次
    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang)
    #用枪打敌人两次
    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang)

main()
