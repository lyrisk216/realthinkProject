#pygame snow V1.0 基础效果
#V1.1 透视效果， 引入比例因子rate为控制变量
#V1.2 wind, add and reduce snow
#V1.3 几何雪花绘制
import pygame, sys, random
#-----defination-----
SNOW_NUM = 500
SNOW_SIZEMAX = 15
SNOW_BEGINY = -50
SNOW_SPEED_MAX = 2
SCREEN_W, SCREEN_H = 1024, 768
SNOW_ADD_NUM = 1100
def draw_hexagon(scr, x0, y0, r, c):
    polygon = ( (int(x0 - r), int(y0)),
                (int(x0 - r * 0.5), int(y0 + r * 0.865)),
                (int(x0 + r * 0.5), int(y0 + r * 0.865)),
                (int(x0 + r), int(y0)),
                (int(x0 + r * 0.5), int(y0 - r * 0.865)),
                (int(x0 - r * 0.5), int(y0 - r * 0.865)) )
    pygame.draw.lines(scr, c, True, polygon, 1)
    return
class CLS_snow(object):
    def __init__(self, c, r, x, y, spdX, spdY, rate):
        self.c = c
        self.r = r
        self.x, self.y = x, y
        self.spdX, self.spdY = spdX, spdY
        self.rate = rate
        self.flag = 0
    def draw(self, scr):
        c = ( int(self.c[0] * self.rate),
              int(self.c[1] * self.rate),
              int(self.c[2] * self.rate) )
        if self.r < 10:
            pygame.draw.circle(scr, c,
                               ( int(self.x), int(self.y) ), int(self.r * self.rate), 0)  
            return

        x0, y0 = self.x, self.y
        r = int(self.r * self.rate)
        pygame.draw.line(scr, c, (int(x0 + r * 0.5), int(y0 - r * 0.865)), \
                                    (int(x0 - r * 0.5), int(y0 + r * 0.865)), 3)
        pygame.draw.line(scr, c, (int(x0 + r * 0.5), int(y0 + r * 0.865)), \
                                    (int(x0 - r * 0.5), int(y0 - r * 0.865)), 3)
        pygame.draw.line(scr, c,
                         (int(x0 - r), int(y0)), (int(x0 + r), int(y0)), 3)
        draw_hexagon(scr, x0, y0, r * 0.8, c)
        draw_hexagon(scr, x0, y0, r * 0.6, c)                 
    def move(self):
        self.x += self.spdX * self.rate
        self.y += self.spdY * self.rate
        if self.y > SCREEN_H + self.r:
            self.y = SNOW_BEGINY
        if self.x > SCREEN_W:
            self.x = -self.r
        if self.x < - self.r:
            self.x = SCREEN_W
def snow_init(snowList):
    for i in range(SNOW_NUM):
        rate = (i + 1) / SNOW_NUM
        snowList.append( create_one_snow(rate) )
def create_one_snow(rate):
        c = (255, 255, 255)
        r = random.randint( 1, SNOW_SIZEMAX )
        x, y = random.randint( 0, SCREEN_W ), SNOW_BEGINY
        spdX, spdY =  random.random() - 0.5, (random.random() * 0.5 + 0.5) * SNOW_SPEED_MAX
        return CLS_snow(c, r, x, y, spdX, spdY, rate)
#--------pygame init--------
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('RT SNOW')
clock = pygame.time.Clock()
#-----data init-----
snowList = []
snow_init(snowList)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for snow in snowList:
                    snow.spdX -= 0.5 + random.random() * 0.5
            if event.key == pygame.K_RIGHT:
                for snow in snowList:
                    snow.spdX += 0.5 + random.random() * 0.5
            if event.key == pygame.K_UP:
                if len(snowList) > SNOW_ADD_NUM + 2:
                    for a in range(SNOW_ADD_NUM):
                        i = random.randint(0, len(snowList) - 2)
                        snowList.pop(i)                
            if event.key == pygame.K_DOWN:
                for a in range(SNOW_ADD_NUM):
                    i = random.randint(0, len(snowList) - 2)
                    rate = (snowList[i].rate + snowList[i + 1].rate) / 2
                    snowList.insert(i, create_one_snow(rate))

    screen.fill( (12, 5, 50) )
    for snow in snowList:
        snow.move( )
        snow.draw(screen)
    pygame.display.update()
    clock.tick(60)

