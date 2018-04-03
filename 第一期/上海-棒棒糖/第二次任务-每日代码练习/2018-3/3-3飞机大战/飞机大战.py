import pygame,time
from pygame.locals import *
import random

class Base(object):
    def __init__(self,screen_temp, x,y , image_name):
        self.x=x
        self.y=y
        self.screen=screen_temp
        self.image=pygame.image.load(image_name)
        self.bullet_list=[]#存储发射出去的子弹对象引用


class BasePlane(Base):
    # 把对象放到屏幕中
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
       #发射子弹在屏幕显示和移动
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界,越界就删除
                #在循环中删除会漏删，因为删除后下一个下标会前移，但是这里的for被重复调用，下一个下标前移后，再次会指向它
                self.bullet_list.remove(bullet)

class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        super().__init__(screen_temp, 210, 700, "./feiji/hero1.png")

    #左移
    def move_left(self):
        self.x-=5
    #右移
    def move_right(self):
        self.x+=5
    #发射子弹
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.direction = "right"  # 用来存储飞机默认的显示方向

    # 把敌机自行移动
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    # 发射子弹
    def fire(self):
        random_num=random.randint(1,100)
        if random_num==8 or random_num==20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 40, y - 20, "./feiji/bullet.png")
    #子弹移动
    def move(self):
        self.y-=5
    #子弹越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "./feiji/bullet1.png")

     # 子弹移动
    def move(self):
        self.y += 5
    #子弹越界
    def judge(self):
        if self.y >852:
            return True
        else:
            return False



def key_control(hero_temp):
        # 获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    hero_temp.move_left()
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    hero_temp.move_right()
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
                    hero_temp.fire()

def main():
    #1.创建窗口，传入三个参数，第一个参数屏幕高宽，第二参数和第三参数为固定写法
    screen=pygame.display.set_mode((480,852),0,32)
    #2.引入背景图片
    background=pygame.image.load('./feiji/background.png')
    #3.创建一个飞机对象
    hero=HeroPlane(screen)
    # 4.创建一个敌机
    enemy = EnemyPlane(screen)
    #把背景图片显示在窗口
    while True:
        #设定需要显示的背景图,第二个参数表示把background的左上角放在screen的0，0位置
        screen.blit(background,(0,0))
        #飞机放在窗口
        hero.display()
        # 敌机放在窗口
        enemy.display()
        enemy.move()
        enemy.fire()
        #更新需要显示的内容
        pygame.display.update()
        #控制键盘
        key_control(hero)
        time.sleep(0.01)
if __name__=='__main__':
    main()

