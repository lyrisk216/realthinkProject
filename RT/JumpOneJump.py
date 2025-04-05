#RealThink lesson
#2D版跳一跳 V1.0
import pygame, sys, random

class CLS_Man(object): #小人类，蓄力和跳跃时都使用
    def __init__(self, c, x, y, w, h):
        self.c = c #color
        self.x, self.y, self.w, self.h = x, y, w, h #(x,y)是man矩形下底中心坐标
        self.state = 0 #man状态，0:play，1:jump，2:falied
        self.pressed = False #jump键（空格）是否按下
        self.pressure = 0 #蓄力参数
        self.accY = 0.1 #重力加速度
        self.score = 0 
    def draw(self, screen): #按照蓄力参数绘制man的形状,蓄力过程矩形变成梯形
        pygame.draw.polygon(screen, self.c, \
            ( (int(self.x - self.w/2 - self.pressure/2), int(self.y)),
              (int(self.x + self.w/2 + self.pressure/2), int(self.y)),
              (int(self.x + self.w/2), int(self.y - self.h + self.pressure)),
              (int(self.x - self.w/2), int(self.y - self.h + self.pressure))), 0)
    def update(self):
        if self.state == 0: #play状态
            if self.pressed and self.pressure < PRESMAX:
                self.pressure += 0.1
            return
        elif self.state == 1: #jump状态
            self.x += self.speedX
            self.y += self.speedY
            self.speedY += self.accY
            if ORGY < self.y < ORGY + 5: #man跳到block高度，5是误差范围，因为下落速度可能很大
                br = bList[-1].rect #br是最新一个block的rect四元组
                if br.left <= man.x <=  br.right:
                    man.score += 1 #如果在block范围内，加1分
                    if br.left + br.w/2 - 3 < man.x < br.right - br.w/2 + 3:
                        man.score += 2 #如果跳进圆心范围再多2分
                    moveback(screen) #屏幕左移
            if self.y > SCREENH:
                man.state = 2 #小人跳空了，state应置为2
        
class CLS_Block(object): #block类，跳跃目标
    def __init__(self, c, rect, state):
        self.c = c #color
        self.rect = pygame.Rect(rect) #初始化成pygame.Rect对象
        self.state = state #block状态，0表示已经被跳，1表示还没有被跳
    def draw(self, screen):
        pygame.draw.rect(screen, self.c, self.rect, 0)
        pygame.draw.rect(screen, (0,255,0), \
            (self.rect.x + self.rect.w//2-1, self.rect.y, 3, self.rect.h), 0)
        
def create_block(): #产生一个新的block
    w = random.randint(30, 100) #block宽
    h = random.randint(30, 60) #block高
    x = ORGX + random.randint(100, 300) #新block与man的距离也是随机数
    y = ORGY #block左上角的y坐标，与man的脚下y坐标一样
    return CLS_Block( (random.randint(100,255),
                       random.randint(100,255),
                       random.randint(100,255)),
                      (x, y, w, h), 1) #按照随机数生成一个block，state为1，没跳过

def moveback(screen): #屏幕左移
    man.y, man.state = ORGY, 0 #man的y坐标与state复位
    bList[-1].state = 0 #最新的block设置为“跳过”
    while man.x >= ORGX: #循环左移到man的x坐标到ORGX原位置为止  
        for event in pygame.event.get(): #屏幕移动时也处理事件遍历
            if event.type == pygame.QUIT: # 鼠标关闭窗口
                pygame.quit()
                sys.exit()
        screen.fill( (0,0,0), (0, 100, SCREENW, SCREENH) ) #SCORE外的部分刷黑准备重新绘制
        man.x -= 1 #man左移
        man.draw(screen)
        for b in bList:
            b.rect.x -= 1 #每个block左移
            b.draw(screen)
        pygame.display.update() #绘制左移动画效果
        clock.tick(200)

# ----- Pygame init -----
SCREENW, SCREENH = 1024, 600 # 窗口大小定义
pygame.init() # pygame初始化函数调用
screen = pygame.display.set_mode( (SCREENW, SCREENH) ) # 产生窗口对象screen
pygame.display.set_caption("jump one jump") # 指定窗口名称
clock = pygame.time.Clock() # 帧率定时器初始化
font = pygame.font.Font(None, 32)# font对象初始化

# ----- Program init -----
ORGX, ORGY = 600, 500 #man原始位置，每次跳完man还会回到这个位置
PRESMAX = 20 #蓄力最大值
man = CLS_Man( (255,255,0), ORGX, ORGY, 8, 30) #生成man对象
bList = [CLS_Block( (0,0,255), (ORGX - 50, ORGY, 100, 40), 0)] #bList是当前所有block，生成脚下block
while True: #主循环    
    for event in pygame.event.get(): #事件遍历
        if event.type == pygame.QUIT: # 鼠标关闭窗口
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #如果有键按下
            if man.state == 0 and event.key == pygame.K_SPACE: #man是play状态并按下空格键
                man.pressed = True #man的pressed状态置为Ture，man.update里会处理蓄力
            elif man.state == 2 and event.key == pygame.K_RETURN: #man是failed状态并按下回车键
                man = CLS_Man( (255,255,0), ORGX, ORGY, 8, 30) #man状态复位
                bList = [CLS_Block( (0,0,255), (ORGX - 50, ORGY, 100, 40), 0)] #blist复位
        elif event.type == pygame.KEYUP: #如果有键松开
            if man.state == 0 and man.pressed == True: #如果man是play状态并正在蓄力
                man.speedX, man.speedY = 0.1 + man.pressure/5, -man.pressure/7 - 2 #跳跃速度初始化
                man.pressed, man.pressure = False, 0 #man的pressed状态与蓄力状态复位
                man.state = 1 #man的state置为jump

    if bList[-1].state == 0: #最后一个block已经跳过了，产生新block
        bList.append( create_block() )  
    screen.fill( (0,0,0) ) #背景涂黑
    img = font.render('SCORE:'+str(man.score), True, (0,255,0))
    screen.blit( img, (100,10) ) #绘制分数
    for b in bList: #绘制每个block
        b.draw(screen)
    man.update() #man参数更新
    man.draw(screen) #绘制man
    pygame.display.update() #屏幕重绘
    clock.tick(300) #帧率建议>=300

    
