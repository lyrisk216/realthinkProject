#canon game
import math, pygame, sys, random
#------main------
SCREEN_W, SCREEN_H = 1024, 600
H = 400
BARREL_LEN = 30

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
spd, deg, g = 1000, 45, -9.8
rate = 1 / 100

sysStatus = 0
tankX = random.randint(500, SCREEN_W)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                deg += 1
            elif event.key == pygame.K_DOWN:
                deg  -= 1
            elif event.key == pygame.K_LEFT:
                spd -= 10
            elif event.key == pygame.K_RIGHT:
                spd += 10
            elif event.key == pygame.K_RETURN:
                x, y = x0, y0
                spdX = spd * math.cos(deg / 180 * math.pi)
                spdY = spd * math.sin(deg / 180 * math.pi)
                sysStatus = 1
            elif event.key == pygame.K_SPACE:
                tankX = random.randint(100, SCREEN_W)
    screen.fill((0, 0, 0))
    if sysStatus == 1:
        spdX -= spdX ** 3 * (0.1 * 10 ** -7)
        x += spdX
        spdY += g
        y += spdY
        pygame.draw.circle(screen, (0, 255, 255), (x * rate, H - y * rate), 2, 0)
        if y <= 0:
            sysStatus = 0
            if abs(x * rate - tankX) < 5:
                print('Bombed!!!')
    x0 = BARREL_LEN * math.cos(deg / 180 * math.pi)
    y0 = BARREL_LEN * math.sin(deg / 180 * math.pi)
    pygame.draw.line(screen, (0, 255, 255), (0, H), (x0, H - y0), 4)
    img = font.render('Angle: ' + str(deg) + 'deg', True, (0, 255, 255))
    screen.blit(img, (0, H + 32))
    img = font.render('Speed: ' + str(spd) + 'm / s', True, (0, 255, 255))
    screen.blit(img, (0, H + 64))
    pygame.draw.rect(screen, (0, 255, 0), (0, H, SCREEN_W, 5), 0)
    pygame.draw.circle(screen, (255, 255, 0), (tankX, H), 3, 0)
    pygame.draw.rect(screen, (0, 255, 255), (0, H + 10, spd / 10, 3), 0)
    pygame.display.update()
    clock.tick(100)
    
    
