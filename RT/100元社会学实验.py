#RT Lesson 100元社会学实验
import pygame, random, sys
SCREEN_W, SCREEN_H = 800, 600
#--- init ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
mList = [100] * 100
w = SCREEN_W // 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill( (0, 0, 0) )

    A = random.randint(0, 99)
    B = random.randint(0, 99)
    mList[A] -= 1
    mList[B] += 1
    for i in range(100):
        pygame.draw.rect(screen, (0, 255, 0),\
            (i * w, 0, w - 1, mList[i]), 0)
    pygame.display.update()
