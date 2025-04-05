#pygame snow V1.0 (Corrected)

import pygame, sys, random

#-----definitions-----
SNOW_NUM = 160
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
        d = random.randint(1, 20)
        c = (199, 199, 199)
        r = (1 / d ** 0.5) * SNOW_SIZEMAX
        x = random.randint(0, SCREEN_W)
        y = SNOW_BEGINY  # Corrected: Start above the screen
        spdX = random.random() * 0.5
        spdY = (1 / d ** 0.5) * SNOW_SPEED_MAX
        snowList.append(CLS_snow(c, r, x, y, spdX, spdY))

#--------pygame init--------
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),flags=0, depth=32)
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
    screen.fill((170, 190, 230))
    for snow in snowList:
        snow.move()
        snow.draw(screen)
    pygame.display.update()
    clock.tick(60)
