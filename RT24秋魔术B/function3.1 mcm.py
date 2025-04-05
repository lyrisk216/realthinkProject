#RT Lesson
#function V3.1

import pygame, sys , random
from math import *
SCREEN_SIZE = (900, 900)

def draw_cs(screen, scale):#画坐标系，sacle是比例尺
    #----- x轴y轴 -----
    pygame.draw.line(screen, (0,0,0), (0, SCREEN_SIZE[1] / 2), \
        (SCREEN_SIZE[0], SCREEN_SIZE[1] / 2))
    pygame.draw.lines(screen, (0,0,0), False, ((SCREEN_SIZE[0] - 5, SCREEN_SIZE[1] / 2 - 5), \
        (SCREEN_SIZE[0], SCREEN_SIZE[1] / 2), (SCREEN_SIZE[0] - 5, SCREEN_SIZE[1] / 2 + 5)))
    pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2, 0), \
        (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1]))
    pygame.draw.lines(screen, (0,0,0), False, ((SCREEN_SIZE[0] / 2 - 5, 5), \
        (SCREEN_SIZE[0] / 2, 0), (SCREEN_SIZE[0] / 2 + 5, 5)))
    #----- 刻度与数字 -----
    step = int(1 / scale * 100)
    for x in range(step, round(SCREEN_SIZE[0] / 2 / scale), step):
        pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2 + x * scale, SCREEN_SIZE[1] / 2), \
            (SCREEN_SIZE[0] / 2 + x * scale, SCREEN_SIZE[1] / 2 - 3))
        pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2 - x * scale, SCREEN_SIZE[1] / 2), \
            (SCREEN_SIZE[0] / 2 - x * scale, SCREEN_SIZE[1] / 2 - 3))        
        imgFont = font.render(str(x), True, (0,0,0))
        screen.blit( imgFont, (SCREEN_SIZE[0] / 2 + x * scale - 4, SCREEN_SIZE[1] / 2 + 2 ))       
        imgFont = font.render(str(-x), True, (0,0,0))        
        screen.blit( imgFont, (SCREEN_SIZE[0] / 2 - x * scale - 8, SCREEN_SIZE[1] / 2 + 2 ))
    for y in range(step, round(SCREEN_SIZE[1] / 2 / scale), step):
        pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 - y * scale), \
            (SCREEN_SIZE[0] / 2 + 3, SCREEN_SIZE[1] / 2 - y * scale))
        pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 + y * scale), \
            (SCREEN_SIZE[0] / 2 + 3, SCREEN_SIZE[1] / 2 + y * scale))       
        imgFont = font.render(str(y), True, (0,0,0))
        screen.blit( imgFont, (SCREEN_SIZE[0] / 2 - 10, SCREEN_SIZE[1] / 2 - y * scale - 8 ))       
        imgFont = font.render(str(-y), True, (0,0,0))        
        screen.blit( imgFont, (SCREEN_SIZE[0] / 2 - 16, SCREEN_SIZE[1] / 2 + y * scale - 8 ))     
    imgFont = font.render('0', True, (0,0,0)) 
    screen.blit( imgFont, (SCREEN_SIZE[0] / 2 - 10, SCREEN_SIZE[1] / 2 + 2))
    imgFont = font.render('x', True, (0,0,0)) 
    screen.blit( imgFont, (SCREEN_SIZE[0] - 10, SCREEN_SIZE[1] / 2 + 4))
    imgFont = font.render('y', True, (0,0,0)) 
    screen.blit( imgFont, (SCREEN_SIZE[0] / 2 - 12, 2))
    #---------曲线颜色编号对照
    for i in range(len(colorList)):
        pygame.draw.rect(screen,colorList[i],((20+i*20,20),(15,15)))
        txtFont=font.render(str(i+1),True,colorList[i])
        screen.blit(txtFont,(25+i*20,40))

def change_x(x, scale):
    return x * scale + SCREEN_SIZE[0] / 2
def change_y(y, scale):
    return SCREEN_SIZE[1] / 2 - y * scale

#画函数曲线，f是f(x)表达式，scale是比例尺，step是x轴点距
def draw_func(screen, f, scale, step, color):
    xd = 0 #xd,yd是屏幕显示坐标
    while xd < SCREEN_SIZE[0]: #x向循环，求y=f(x)
        x = (xd - SCREEN_SIZE[0] / 2) / scale
        try:#可能会出现除零错误
            y = eval(f)
            yd = SCREEN_SIZE[1] / 2 - y * scale
            screen.set_at((int(xd), int(yd)), color)
        except:
            pass
        xd += step
        
def refresh( screen, scale, step, dList ):
    screen.fill( (240, 240, 240) ) #背景绘制
    draw_cs(screen, scale) #画坐标系
    for i in range(len(fList)): #画所有函数曲线
        draw_func(screen, fList[i], scale, step, colorList[i])
    for d in dList:
        c = [0, 128, 64]
        x, y = d[0], d[1]
        pygame.draw.line(screen, c, (change_x(x, scale) - 3, change_y(y, scale) - 3),
                                    (change_x(x, scale) + 3, change_y(y, scale) + 3), 3)
        pygame.draw.line(screen, c, (change_x(x, scale) + 3, change_y(y, scale) - 3),
                                    (change_x(x, scale) - 3, change_y(y, scale) + 3), 3)
        #print(x, y, change_x(x, scale), change_y(y, scale))
    pygame.display.update() #画面刷新    

def get_RSD(dList,a,b):
    s = 0
    for d in dList:
        s += (d[1] - (a*d[0]+b)) ** 2
    return s
    
def find_func(dList,cnt,lt,rt):
    global fList
    ansList = []
    for i in range(cnt):
        a=random.random()*(rt[0]-lt[0])+lt[0]
        b=random.random()*(rt[1]-lt[1])+lt[1]
        s=get_RSD(dList,a,b)
        for j in range(len(ansList)):
            if s<ansList[j][2]:
                ansList.insert(j,[a,b,s])
                break
        if len(ansList)<5:
            ansList.append([a,b,s])
        if len(ansList)>5:
            ansList.pop(-1)
    for i in range(5):
        fList[i]=str(ansList[i][0])+'*x'
        if ansList[i][1]>=0:
            fList[i]+='+'
        fList[i]+=str(ansList[i][1])
        print(str(i+1)+': '+fList[i])
    return ansList

def get_RSD2(dList,a,b,c):
    s = 0
    for d in dList:
        s += (d[1] - (a*d[0]**2+b*d[0]+c)) ** 2
    return s
    
def find_func2(dList,cnt,lt,rt):
    global fList
    ansList = []
    for i in range(cnt):
        a=random.random()*(rt[0]-lt[0])+lt[0]
        b=random.random()*(rt[1]-lt[1])+lt[1]
        c=random.random()*(rt[2]-lt[2])+lt[2]
        s=get_RSD2(dList,a,b,c)
        for j in range(len(ansList)):
            if s<ansList[j][2]:
                ansList.insert(j,[a,b,c,s])
                break
        if len(ansList)<5:
            ansList.append([a,b,c,s])
        if len(ansList)>5:
            ansList.pop(-1)
    for i in range(5):
        fList[i]=str(ansList[i][0])+'*x**2'
        if ansList[i][1]>=0:
            fList[i]+='+'
        fList[i]+=str(ansList[i][1])+'*x'
        if ansList[i][2]>=0:
            fList[i]+='+'
        fList[i]+=str(ansList[i][2])
        print(str(i+1)+': '+fList[i])
    return ansList
#----- pygame初始化
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("RT Funtion V3.1")
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock() 

#----- 程序初始化
f = open('data.txt', 'r')
strList = f.readlines()
f.close()
dList = []
for dataStr in strList:
    x, y = dataStr.split(',')
    dList.append( [eval(x), eval(y)] )
    dList[-1][0]-=1959
    dList[-1][1]-=315
print(dList)

colorList = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]
fList = [''] * 6 #支持6个函数
scaleList = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001]
scaleNum = 0
scale = 100
step = 0.5 #初始化x轴点距
refresh( screen, scale, step, dList)

while True:#主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                step /= 1.5 #提高点距
            elif event.key == pygame.K_RIGHT:
                step *= 1.5 #缩小点距
            elif event.key == pygame.K_UP and scaleNum < len(scaleList) - 2:
                scaleNum += 1 #增大比例尺
                scale = scaleList[scaleNum]
            elif event.key == pygame.K_DOWN and scaleNum > 0:
                scaleNum -= 1 #缩小比例尺
                scale = scaleList[scaleNum]
            elif ord('1') <= event.key <= ord('6'):
                s = 'No.' + chr(event.key) + '  f(x)='
                fList[event.key - 49] = input(s)
            elif event.key == pygame.K_RETURN:
                #find_func(dList,10000,[1,0],[5,5])
                find_func2(dList,10000,[0,0,0],[0.07,10,1])
            refresh( screen, scale, step, dList )
    clock.tick(100)
