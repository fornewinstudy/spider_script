import pygame,sys
from pygame.locals import QUIT
from pygame.locals import KEYDOWN
import time

# 子弹类型
class Bullet(object):
    # 构造方，用于初始化子弹对象的属性
    def __init__(self,screen_temp,x,y):
        self.x = x + 40   # 子弹起始x坐标
        self.y = y - 20   # 子弹起始y坐标
        self.screen = screen_temp   #窗口
        self.image = pygame.image.load("./images/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))    # 显示子弹图片
    # 子弹移动方法
    def move(self):
        self.y-=10  # 子弹y坐标自减10
    # 判断子弹是否越界的方法
    def judge(self):
        if self.y:          # 如果子弹的y坐标小于0
            return True     # 返回True
        else:
            return False    # 返回False

# 玩家飞机
class Aircraft_obj(object):
    # 构造方法，初始化飞机对象的属性
    def __init__(self,screen_temp):
        self.x = 190                    # 飞机起始x坐标
        self.y = 708                    # 飞机起始y坐标
        self.screen = screen_temp       # 窗口
        self.image = pygame.image.load("./images/hero1.png")   # 创建一个飞机图片
        self.bullet_list = []   # 存储发射出去的子弹对象
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()    # 显示子弹
            bullet.move()       # 移动子弹
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)     # 删除子弹
    # 飞机左移方法
    def move_left(self):
        if self.x < 10:     # x坐标小于10（移动距离）
            pass            # 不做任何事
        else:
            self.x-= 10     # X坐标自然减少10
    # 飞机右移的方法
    def move_right(self):
        if self.x > 480-100-10:     # x坐标大于（窗口宽度-飞机宽度-移动距离）的值
            pass                    # 不做任何事
        else:
            self.x += 10
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))  #将发射的子弹对象存储到bullet_list中

# 敌方飞机
class EnemyPlane(object):
    # 构造方法，初始化敌机的属性
    def __init__(self,screen_temp):
        self.x = 0     # 敌机的起始x坐标
        self.y = 0     # 敌机的起始y坐标
        self.screen = screen_temp       # 窗口
        self.image = pygame.image.load("./images/enemy0.png")   # 创建一个敌机图片
        self.direction = 'right'        # 用来存储飞机的移动方向，默认向右移
        # 爆炸效果用的属性
        self.hit = False        # 表示是否要爆炸
        self.bomb_lists = []    # 用来存储爆炸时需要的图片
        self. _crate_images()  # 调用这个方法向bomb_lists中添加图片
        self.image_num = 0      # 用来记录while循环的的次数，当次数达到一定值时才能显示一张爆炸的图，然后清空
        self.image_index = 0    # 用来记录当前要显示的爆炸效果的图片的序号
    #敌机移动的方法
    def move(self):
        if self.hit == True:       # 如果被击中，敌机不移动
            pass
        else:
            if self.direction == "right":   # 如果是向右移动
                self.x += 5                 # x坐标自增加5
            elif self.direction == "left":  # 如果是向左移动
                self.x -= 5                 # x坐标自减少5
            if self.x > 480-50:             # 如x坐标大于窗口减去敌机宽度的值
                self.direction = 'left'     # 移动方向改为左
            elif self.x < 0:                # 如果x坐标小于0
                self.direction = 'right'    # 移动方向改为右
    # 将爆炸需要的图片添加到self.bomb_lists中。
    def _crate_images(self):
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down1.png"))
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down2.png"))
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down3.png"))
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down4.png"))
    # 判断爆炸的方法，x1为子弹最左侧的横坐标，x2为子弹最右侧的横坐标，y为子弹当前的纵坐标
    def blast(self,x1,x2,y):
        # 判断子弹能命中敌机的三种情况（51是敌机图片的宽度，39是敌机图片的高度）
        if((x1>=self.x and x2 <= self.x+51) or x2 ==self.x or x1 == self.x + 51) and y < 39:
            self.hit = True
    def display(self):
        # 如果被击中就显示爆炸效果，否则显示普通飞机效果
        if self.hit == True:        # 如果满足爆炸条件，就显示爆炸的图片
            self.screen.blit(self.bomb_lists[self.image_index],(self.x,self.y))
            self.image_num += 1         # 统计循环次数，为了使玩家看清爆炸效果
            if self.image_num == 7:     # 如果循环次数达到7次
                self.image_num = 0      # 将循环次数改为0次
                self.image_index += 1   # 图片显示次数加1，换为另外一张图片
            if self.image_index > 3:    # 如果图片序号大于3（一共4张图片）
                time.sleep(1)           # 暂停一秒
                exit()                  # 调用exit退出游戏
        else:                           # 否则显示正常的敌机图片
            self.screen.blit(self.image,(self.x,self.y))

    # 处理鼠标和键盘事件的方法
    def key_control(aircraft_temp):
        # 获得当前等待处理的事件，使用for循环遍历里面的事件
        for event in pygame.event.get():
            #判断是否点击了退出按钮
            if event.type == QUIT:
                print("exit")       # 输出“exit”
                exit()              # 退出窗口
            # 判断是不是键盘按下的事件
            elif event.type == KEYDOWN:
                # pass
                # 检测按键是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print("left")               # 输出“left”
                    aircraft_temp.move_left()   # 执行飞机左移方法
                # 检测按键是d或者right
                elif event.key == k_d or event.key == K_RIGHT:
                    print("right")          # 输出“right”
                    aircraft_temp.move_right()    # 执行飞机右移方法
                # # 检测按键是不是空格键
                elif event.key == K_SPACE:
                    print("space")          # 输出“space”
                    aircraft_temp.fire()    # 执行飞机类中存储子弹的方法

# 创建窗口
def main():
    pygame.init()  # 初始化 pygame
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 创建一个背景图片
    background = pygame.image.load("./images/background.png")
    # 创建一个玩家飞机对象
    aircraft = Aircraft_obj(screen)
    # 创建一个敌机对象
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        aircraft.display()
        for bullet in aircraft.bullet_list:
            x1 = bullet.x
            x2 = bullet.x + 22
            y1 = bullet.y
            enemy.blast(x1, x2, y1)
        enemy.display()
        enemy.move()
        pygame.display.update()
        key_control(aircraft)
        time.sleep(0.01)

main()


































