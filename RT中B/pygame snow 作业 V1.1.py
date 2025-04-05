#pygame snow V1.0 基础效果
#V1.1 透视效果， 引入比例因子rate为控制变量
import pygame, sys, random
#-----defination-----
SNOW_NUM = 1000
SNOW_SIZEMAX = 15
SNOW_BEGINY = -50
SNOW_SPEED_MAX = 2
SCREEN_W, SCREEN_H = 1024, 768
ADD_SCREEN = 500
class CLS_snow(object):
    def __init__(self, c, r, x, y, spdX, spdY, rate):
        self.c = c
        self.r = r
        self.x, self.y = x, y
        self.x_init = x
        self.spdX, self.spdY = spdX, spdY
        self.rate = rate
    def draw(self, scr):
        c = ( int(self.c[0] * self.rate),
              int(self.c[1] * self.rate),
              int(self.c[2] * self.rate) )
        pygame.draw.circle(scr, c, ( int(self.x), int(self.y) ), int(self.r * self.rate), 0)  
    def move(self):
        self.x += self.spdX * self.rate
        self.y += self.spdY * self.rate
        if self.y > SCREEN_H + self.r:
            self.y = SNOW_BEGINY
            self.x = self.x_init
def snow_init(snowList, num):
    snowList.clear()
    for i in range(num):
        rate = (i + 1) / num
        c = (255, 255, 255)
        r = random.randint( 1, SNOW_SIZEMAX )
        x, y = random.randint( 0 - ADD_SCREEN, SCREEN_W + ADD_SCREEN ), random.randint( 0, SCREEN_H )
        spdX, spdY =  0, (random.random() * 0.5 + 0.5) * SNOW_SPEED_MAX
        snowList.append(CLS_snow(c, r, x, y, spdX, spdY, rate))
def snow_spd_change(dspdX, dspdY):
    for snowflake in snowList:
        snowflake.spdX += dspdX
#--------pygame init--------
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('RT SNOW')
clock = pygame.time.Clock()
#-----data init-----
snowList = []
snow_init(snowList, SNOW_NUM)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snow_spd_change(-1, 0)
            if event.key == pygame.K_RIGHT:
                snow_spd_change(1, 0)
            if event.key == pygame.K_UP:
                snow_init(snowList, len(snowList) + 500)
            if event.key == pygame.K_DOWN:
                snow_init(snowList, len(snowList) - 500)
    screen.fill((12, 5, 50))
    for snow in snowList:
        snow.move( )
        snow.draw(screen)
    pygame.display.update()
    clock.tick(60)

