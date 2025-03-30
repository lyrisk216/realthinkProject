#pygame snow V1.0

import pygame, sys, random

#-----defination-----
SNOW_NUM = 500
SNOW_SIZEMAX = 15
SNOW_BEGINY = -50
SNOW_SPEED_MAX = 2
SCREEN_W, SCREEN_H = 1024, 768
class CLS_snow(object):
    def __init__(self, c, r, x, y, spdX, spdY):
        self.c = c
        self.r = r
        self.x, self.y = x, y
        self.x_init = x
        self.spdX, self.spdY = spdX, spdY
    def draw(self, scr):
        pygame.draw.circle(scr, self.c, (int(self.x), int(self.y)), self.r, 0)
    def move(self):
        self.x += self.spdX
        self.y += self.spdY + random.random() * 0.2
        if self.y > SCREEN_H + self.r:
            self.y = SNOW_BEGINY
            self.x = self.x_init
def snow_init(snowList):
    for i in range(SNOW_NUM):
        d = random.random() * 19 + 1
        gray = int(210 + (1 / d**2) * 45)
        c = (gray, gray, gray)
        r = (1 / d ) * SNOW_SIZEMAX
        x, y = random.randint(0, SCREEN_W), random.randint(0, SCREEN_H)
        spdX, spdY =  (1 / d ) *(random.random() * 1.4 - 0.7), (1 / d ) * SNOW_SPEED_MAX
        snowList.append(CLS_snow(c, r, x, y, spdX, spdY))
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
    screen.fill((120, 140, 200))

    #排序, 近的后画
    for a in range(len(snowList) - 1):
        flag = 0
        for i in range(len(snowList) - a - 1):
            if snowList[i].r > snowList[i + 1].r:
                snowList[i], snowList[i + 1] = snowList[i + 1], snowList[i]
                flag = 1
        if flag == 0:
            break

    for snow in snowList:
        snow.move( )
        snow.draw(screen)
    pygame.display.update()
    clock.tick(60)
