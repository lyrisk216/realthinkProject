import pygame, sys, random
def new_circle():
    x = random.randint(MAX_R, SCREEN_W - MAX_R)
    y = random.randint(MAX_R, SCREEN_H - MAX_R)
    r = random.randint(MIN_R, MAX_R)
    return x, y, r
#------main------
SCREEN_W, SCREEN_H = 800, 600 #屏幕尺寸
MIN_R, MAX_R = 150, 100 #圆的半径上下限
pygame.init() #pygame初始化函数
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock() #帧率定时器初始化
font = pygame.font.Font(None, 64) #font对象初始化
gameTime = 5000 #游戏时长， 单位毫秒
score = 0
sysStatus = 0 #游戏状态， 0：wait, 1:play
while True:
    for event in pygame.event.get(): #事件遍历
        if event.type == pygame.QUIT: #点×关闭窗口
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if sysStatus == 0 and event.button == 3: #鼠标右键开始
                sysStatus = 1 #切换到status play
                score = 0
                x, y, r = new_circle() #得到新随机圆参数
                time0 = pygame.time.get_ticks() #获得当前时间
            if sysStatus == 1 and event.button == 1: #鼠标左键点击圆
                mouseX, mouseY = event.pos[0], event.pos[1] #获得鼠标位置
                if (mouseX - x) ** 2 + (mouseY - y) ** 2 < r ** 2:
                    score += 1 #点中了， 得分
                    x, y, r = new_circle() #得到新随机圆参数
    screen.fill((0, 0, 0))
    if sysStatus == 0: #status wait
        imgText = font.render('score: ' + str(score) + '...Click Right to start',
                              True, (0, 255, 0))
        screen.blit(imgText, (100, 300))
    else: #status play
        imgText = font.render('score: ' + str(score), True,(0, 255, 0))
        screen.blit(imgText, (0, 0))
        t = (gameTime - (pygame.time.get_ticks() - time0)) / 1000
        if t < 0: #如果时间已用完， 本局结束
            sysStatus = 0 #切换到status wait
        imgText = font.render('time:' + str(t), True, (0, 0, 255))
        screen.blit(imgText, (400, 0))
        pygame.draw.circle(screen, (135, 206, 235), (x, y), r, 0)
    pygame.display.update() #屏幕刷新
    clock.tick(100) #帧率可调
        
