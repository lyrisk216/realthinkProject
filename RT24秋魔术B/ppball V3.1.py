#RT Lesson ppball
#V3.0 变速运动物理研究
#V3.1 考虑空气阻力
import pygame, sys, random
SCREEN_W, SCREEN_H = 1024, 600
BORDER_W = 10
ACCURACY = 2 #add in V1.0
G = 0.01 #重力加速度 add in V1.1
SPEEDY_MAX = 3 #add in V1.1
def set_new_ball(ball): #add in V1.0
    ball.x, ball.y = 10, 10
    ball.spdX = 3
    ball.spdY = 0    
#绘图函数，对指定像素集pixel，在坐标(x0,y0)以scale大小绘图
def RT_draw(screen, pixel, x0, y0, scale):
    color = ( pygame.color.THECOLORS['black'],              
              pygame.color.THECOLORS['gray32'],
              pygame.color.THECOLORS['gray64'],
              pygame.color.THECOLORS['white'],
              pygame.color.THECOLORS['red'],
              pygame.color.THECOLORS['green'],
              pygame.color.THECOLORS['blue'],
              pygame.color.THECOLORS['orange'],
              pygame.color.THECOLORS['brown'],
              pygame.color.THECOLORS['purple'],
              pygame.color.THECOLORS['yellow'],
              pygame.color.THECOLORS['cyan'],
              pygame.color.THECOLORS['sienna'],
              pygame.color.THECOLORS['chocolate'],
              pygame.color.THECOLORS['coral'],
              pygame.color.THECOLORS['darkgreen'] )
    for y in range(len(pixel)): # 在高度方向循环
        line = pixel[y] # 第y行像素字符串
        for x in range(len(line)): # 在宽度方向循环
            if 'A' <= line[x] <= 'F':
                c = color[ord(line[x]) - 55]
            elif '0' <= line[x] <= '9':
                c = color[eval(line[x])] # 取得颜色编号
            else:
                continue            
            pygame.draw.rect(screen, c,
                             (int(x*scale+x0), int(y*scale+y0), scale, scale), 0)
class CLS_ball( object ): # 小球类定义
    def __init__( self, x, y, spdX, spdY, scale ):  # 小球初始化
        self.x, self.y = x, y
        self.spdX, self.spdY = spdX, spdY
        self.scale = scale
        self.w, self.h = 0, 0
        self.interval = 8 #动画时间间隔
        self.counter = 0 #动画计数器
        self.picList = [] #动画list
    def add_pic( self, pixel ):
        self.picList.append( pixel )
        self.w = len(pixel[0]) * self.scale #根据scale计算实际宽高
        self.h = len(pixel) * self.scale
    def move( self ):
        self.x += self.spdX
        self.spdY += G 
        if self.spdY > SPEEDY_MAX:
            self.spdY = SPEEDY_MAX
        self.y += self.spdY
        if self.x < BORDER_W or self.x > SCREEN_W - self.w - BORDER_W: 
            self.spdX *= -1 # 速度取反
        if self.y > SCREEN_H - self.h - BORDER_W: # y方向出界
            self.spdY *= -1 # 速度取反     
    def move_in_air( self ):   # 小球坐标计算
        airX = 0.0001 * self.spdX ** 2
        if self.spdX > 0:
            self.spdX -= airX
        else:
            self.spdX += airX
        self.x += self.spdX
        airY = 0.0001 * self.spdY ** 2
        if self.spdY > 0:
            self.spdY += (G - airY)
        else:
            self.spdY += (G + airY)
        self.y += self.spdY
        if self.x < BORDER_W or self.x > SCREEN_W - self.w - BORDER_W: 
            self.spdX *= -1 # 速度取反
        if self.y > SCREEN_H - self.h - BORDER_W: # y方向出界
            self.spdY *= -1 # 速度取反
    def draw( self, scr ):
        RT_draw( scr, \
            self.picList[int(self.counter) // self.interval % len(self.picList)], \
            self.x, self.y, self.scale)
        self.counter += self.spdX * 0.5
def draw_field( scr ): # 绘制场地
    c = pygame.color.THECOLORS['brown']
    pygame.draw.rect(scr,c,(0, SCREEN_H - BORDER_W, SCREEN_W, BORDER_W), 0)
    pygame.draw.rect(scr,c,(0, 0, BORDER_W, SCREEN_H), 0)
    pygame.draw.rect(scr,c,(SCREEN_W - BORDER_W, 0, BORDER_W, SCREEN_H), 0)
#----- pygame init -----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("RT - PingPong Ball") #窗口命名
clock = pygame.time.Clock()
#----- data init -----
ball = CLS_ball(10, 10, 2, 2, 3)  
ball2 = CLS_ball(10, 10, 2, 2, 4)

pixel = []
pixel.append('....DD....')
pixel.append('..DDAADD..')
pixel.append('.DDDAADDD.')
pixel.append('.DDDAADDD.')
pixel.append('DDDDAADDDD')
pixel.append('DDDDAADDDD')
pixel.append('.DDDAADDD.')
pixel.append('.DDDAADDD.')
pixel.append('..DDAADD..')
pixel.append('....DD....')
ball.add_pic( pixel )       # 把第1幅图片放到动画列表中
ball2.add_pic( pixel )

pixel = [ ]
pixel.append('....DD....')
pixel.append('..DDDDDD..')
pixel.append('.DDDDDDAD.')
pixel.append('.DDDDDAAD.')
pixel.append('DDDDDAADDD')
pixel.append('DDDDAADDDD')
pixel.append('.DDAADDDD.')
pixel.append('.DAADDDDD.')
pixel.append('..DDDDDD..')
pixel.append('....DD....')
ball.add_pic( pixel )       # 把第2幅图片放到动画列表中
ball2.add_pic( pixel )

pixel = [ ]
pixel.append('....DD....')
pixel.append('..DDDDDD..')
pixel.append('.DDDDDDDD.')
pixel.append('.DDDDDDDD.')
pixel.append('DAAAAAAAAD')
pixel.append('DAAAAAAAAD')
pixel.append('.DDDDDDDD.')
pixel.append('.DDDDDDDD.')
pixel.append('..DDDDDD..')
pixel.append('....DD....')
ball.add_pic( pixel )       # 加：把第3幅图片放到动画列表中
ball2.add_pic( pixel )

pixel = [ ]
pixel.append('....DD....')
pixel.append('..DDDDDD..')
pixel.append('.DADDDDDD.')
pixel.append('.DAADDDDD.')
pixel.append('DDDAADDDDD')
pixel.append('DDDDAADDDD')
pixel.append('.DDDDAADD.')
pixel.append('.DDDDDAAD.')
pixel.append('..DDDDDD..')
pixel.append('....DD....')
ball.add_pic( pixel )       # 加：把第4幅图片放到动画列表中
ball2.add_pic( pixel )

set_new_ball(ball)
set_new_ball(ball2)
while True: #----- main loop -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            '''
            if event.key == pygame.K_UP:
                paddle.accY = -0.2 #modified in V1.2
            elif event.key == pygame.K_DOWN:
                paddle.accY = 0.2 #modified in V1.2
            elif event.key == pygame.K_SPACE:#add in V1.0
                set_new_ball(ball)
            '''
            pass
    screen.fill((0,64,0))
    draw_field( screen ) 
    ball.move( )
    ball.draw( screen ) 
    ball2.move_in_air( )
    ball2.draw( screen ) 
    pygame.display.update()
    clock.tick(100)
