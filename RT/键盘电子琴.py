#RealThink lesson 键盘电子琴
#piano V0.9 只支持 Do Re

import pygame, sys
#----- Pygame init -----
pygame.init()
pianoImg = pygame.image.load('piano.bmp')
screen = pygame.display.set_mode( pianoImg.get_size() )
pygame.display.set_caption('RT-PIANO')
Do = pygame.mixer.Sound('c4.ogg')
Re = pygame.mixer.Sound('d4.ogg')
Mi = pygame.mixer.Sound('e4.ogg')
Fa = pygame.mixer.Sound('f4.ogg')
Sol = pygame.mixer.Sound('g4.ogg')
La = pygame.mixer.Sound('a4.ogg')
Ti = pygame.mixer.Sound('b4.ogg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Do.play()
                if event.key == pygame.K_2:
                    Re.play()
                if event.key == pygame.K_3:
                    Mi.play()
                if event.key == ord('4'):
                    Fa.play()
                    
    screen.blit(pianoImg, (0, 0))
    pygame.display.update()
