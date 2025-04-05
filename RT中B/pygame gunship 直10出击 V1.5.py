#RT Lesson 直10出击 pygame gunship
# V0.9 能控制飞行， 无碰撞逻辑




import pygame, sys, random
#definition
SCREEN_W, SCREEN_H = 1000, 600
SPACE_UP, SPACE_DOWN = 110, 540
SPEEDY_MAX = 5
BG_COLOR, BORDER_COLOR = (0, 0, 80), (80, 80, 80)
G = 0.5
STONE_H_MIN, STONE_H_MAX, STONE_W = 50, 200, 20
STONE_SPACE = 160
GUNSHIP_HP_MAX = 100
#scoreList = []


class CLS_gunship(object):
    def __init__(self, picFile, x, y, w, h, interval, frameNum):
        pic = pygame.image.load(picFile)
        pic.set_colorkey((0, 0, 0))
        self.pic = pic
        self.x, self.y, self.w, self.h = x, y, w, h
        self.interval, self.frameNum = interval, frameNum
        self.counter = 0
        self.spdX = 3
        self.spdY, self.accY = 0, 0
        self.hp = GUNSHIP_HP_MAX
    def move(self):
        self.spdY += (self.accY + G)
        if self.spdY < -SPEEDY_MAX:
            self.spdY = -SPEEDY_MAX
        elif self.spdY > SPEEDY_MAX:
            self.spdY = SPEEDY_MAX
        self.y += self.spdY
        if self.y < SPACE_UP:
            self.y = SPACE_UP
        if self.y > SPACE_DOWN - self.h:
            fwork.status = 1
            fwork.update_score()
    def draw(self, scr):
        currentNum = (self.counter // self.interval) % self.frameNum
        self.counter += 1
        if fwork.status == 1:
            currentNUM = 4
        scr.blit( self.pic, ( int(self.x), int(self.y) ),
                    ( 0, currentNum * self.h, self.w, self.h) )

        pygame.draw.rect(scr, (0, 255, 0),
                         (self.x, self.y + 36, GUNSHIP_HP_MAX, 5), 1)
        lifeColor = int(self.hp / GUNSHIP_HP_MAX * 255)
        pygame.draw.rect(scr, (255 - lifeColor, lifeColor, 0),
                         (self.x, self.y + 36, self.hp, 5), 0)
class CLS_stone(object):
    def __init__(self):
        self.x, self.w = SCREEN_W, STONE_W
        h = random.randint(STONE_H_MIN, STONE_H_MAX)
        self.h = h
        if h % 2 == 0:
            self.y = SPACE_UP
        else:
            self.y = SPACE_DOWN - h
    def move(self):
        self.x -= fwork.z10.spdX
    def draw(self, scr):
        pygame.draw.rect(scr, (80, 80, 80), (self.x, self.y, self.w, self.h), 0)
class CLS_framework(object):               
    def __init__(self):
        pygame.init()
        self.scr = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption('RT GUNSHIP')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('simkai.ttf', 32)
        self.score = 0
        self.z10 = CLS_gunship('gunship.bmp', 40, 100, 84, 30, 3, 4)
        self.stoneList = []
        self.status = 0
        self.face = pygame.image.load('face.bmp')
        self.hiScoreList = ['0', '0', '0']
    def play(self):
        if self.status == 1:
            return
        self.draw_field()
        self.stone_do()
        self.z10.move()
        self.z10.draw(self.scr)
        pygame.display.update()
        self.clock.tick(100)
    def draw_field(self):
        self.scr.fill((0, 0, 0))
        pygame.draw.rect(self.scr, BG_COLOR, (0, SPACE_UP, SCREEN_W, SPACE_DOWN - SPACE_UP), 0)
        pygame.draw.rect(self.scr, BORDER_COLOR, (0, SPACE_DOWN, SCREEN_W, 10), 0)
        pygame.draw.rect(self.scr, BORDER_COLOR, (0, SPACE_UP - 10, SCREEN_W, 10), 0)
        img = self.font.render('SCORE: ' + str(self.score), True, (160, 180, 0))
        self.scr.blit(img, (SCREEN_W - 280, 50))

        self.scr.blit( self.face, (0, 0) )
        img = self.font.render('Hi-SCORE: ' + self.hiScoreList[0] , True, (255, 0, 0))
        self.scr.blit( img, ( SCREEN_W - 328, 10 ) )

        img = self.font.render('No.1  ' + self.hiScoreList[0] , True, (255, 0, 0))
        self.scr.blit(img, ( SCREEN_W - 240, 120 ) )

        img = self.font.render('No.2  ' + self.hiScoreList[1] , True, (255, 0, 0))
        self.scr.blit(img, ( SCREEN_W - 240, 160 ) )

        img = self.font.render('No.3  ' + self.hiScoreList[2] , True, (255, 0, 0))
        self.scr.blit(img, ( SCREEN_W - 240, 200 ) )
    def stone_do(self):
        lastStoneX = 0
        for stone in self.stoneList:
            stone.move()
            stone.draw(self.scr)
            lastStoneX = stone.x
            if stone.x + stone.w < 0:
                self.stoneList.pop(0)
                
            if (self.z10.x + self.z10.w >= stone.x) and (self.z10.x <= stone.x + stone.w):
                if (self.z10.y + self.z10.h >= stone.y) and (self.z10.y <= stone.y + stone.h):
                    self.z10.hp -= 1
                    if self.z10.hp <= 0:
                        self.status = 1
                        self.update_score()
                        img = self.font.render('Press ENTER to Continue', True, ( 255, 0, 0))
                        self.scr.blit(img, (200, 300))
                else:
                    self.score += stone.h * self.z10.spdX
         
        if SCREEN_W - lastStoneX > random.randint(STONE_SPACE, int(STONE_SPACE * 1.5)):
            stone = CLS_stone()
            self.stoneList.append(stone)
    def update_score(self):
        if self.score >= int(self.hiScoreList[0]):
            self.hiScoreList.insert(0, str(self.score))
            self.hiScoreList.pop(3)
        elif self.score >= int(self.hiScoreList[1]):
            self.hiScoreList.insert(1, str(self.score))
            self.hiScoreList.pop(3)
        elif self.score >= int(self.hiScoreList[2]):
            self.hiScoreList.insert(2, str(self.score))
            self.hiScoreList.pop(3)
    def keydown(self, key):
        if event.key == pygame.K_UP:
            self.z10.accY = -1
        if event.key == pygame.K_LEFT:
            self.z10.spdX -= 1
        if event.key == pygame.K_RIGHT:
            self.z10.spdX += 1
        if event.key == pygame.K_RETURN:
            self.status, self.score = 0, 0
            self.stoneList = []
            self.z10.y = SCREEN_H // 3
            self.z10.hp = GUNSHIP_HP_MAX
    def keyup(self, key):
        if event.key == pygame.K_UP:
            self.z10.accY = 0
#------------------------------
fwork = CLS_framework()
try:
    f = open('score V1.5.txt', 'r')
    fwork.hiScoreList = f.read().split()
    f.close()
except:
    f = open('score V1.5.txt', 'w')
    f.write('0 0 0')
    f.close()
    
pygame.mixer.music.load("See You Again 2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            f = open('score V1.5.txt', 'w')
            f.write(str(fwork.hiScoreList[0]) + ' ' + str(fwork.hiScoreList[1]) + ' ' + str(fwork.hiScoreList[2]))
            f.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            fwork.keydown(event.key)
        elif event.type == pygame.KEYUP:
            fwork.keyup(event.key)
    fwork.play()
    
        

