#RT Lesson
#function V1.4

import pygame, sys 
from math import *
SCREEN_SIZE = (1024, 768)

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
    for x in range(1, round(SCREEN_SIZE[0] / 2 / scale)):
        pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2 + x * scale, SCREEN_SIZE[1] / 2), \
            (SCREEN_SIZE[0] / 2 + x * scale, SCREEN_SIZE[1] / 2 - 3))
        pygame.draw.line(screen, (0,0,0), (SCREEN_SIZE[0] / 2 - x * scale, SCREEN_SIZE[1] / 2), \
            (SCREEN_SIZE[0] / 2 - x * scale, SCREEN_SIZE[1] / 2 - 3))        
        imgFont = font.render(str(x), True, (0,0,0))
        screen.blit( imgFont, (SCREEN_SIZE[0] / 2 + x * scale - 4, SCREEN_SIZE[1] / 2 + 2 ))       
        imgFont = font.render(str(-x), True, (0,0,0))        
        screen.blit( imgFont, (SCREEN_SIZE[0] / 2 - x * scale - 8, SCREEN_SIZE[1] / 2 + 2 ))
    for y in range(1, round(SCREEN_SIZE[1] / 2 / scale)):
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
        
def refresh( screen, scale, step ):
    screen.fill( (240, 240, 240) ) #背景绘制
    draw_cs(screen, scale) #画坐标系
    for i in range(len(fList)): #画所有函数曲线
        draw_func(screen, fList[i], scale, step, colorList[i])    
    pygame.display.update() #画面刷新    
        
#----- pygame初始化
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("RT Funtion V1.0")
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock() 

#----- 程序初始化
colorList = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]
fList = [''] * 6 #支持6个函数
scale = 50 #初始化比例尺，50像素为1
step = 0.5 #初始化x轴点距
refresh( screen, scale, step )

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
            elif event.key == pygame.K_UP:
                scale *= 1.5 #增大比例尺
            elif event.key == pygame.K_DOWN:
                scale /= 1.5 #缩小比例尺
            elif ord('1') <= event.key <= ord('6'):
                s = 'No.' + chr(event.key) + '  f(x)='
                fList[event.key - 49] = input(s)
            refresh( screen, scale, step )
    clock.tick(100)
