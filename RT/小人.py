#RT Lesson

import pygame, sys

def RT_draw(screen, pixel, x0, y0, scale):
    color = ( pygame.color.THECOLORS['black'],
              pygame.color.THECOLORS['gray32'],
              pygame.color.THECOLORS['gray64'],
              pygame.color.THECOLORS['white'],
              pygame.color.THECOLORS['red'],
              pygame.color.THECOLORS['green'],
              pygame.color.THECOLORS['blue'],
              pygame.color.THECOLORS['orange'],
              pygame.color.THECOLORS['brown'],
              pygame.color.THECOLORS['purple'],
              pygame.color.THECOLORS['yellow'],
              pygame.color.THECOLORS['cyan'],
              pygame.color.THECOLORS['chocolate'],
              pygame.color.THECOLORS['coral'],
              pygame.color.THECOLORS['darkgreen'])
    for y in range(len(pixel)):
        line = pixel[y]
        for x in range(len(line)):
            if 'A' <= line[x] <= 'F':
                c = color[ord(line[x]) - 55]
            elif '0' <= line[x] <= '9':
                c = color[eval(line[x])]
            else:
                continue
            pygame.draw.rect(screen, c,\
                (int(x * scale + x0), int(y * scale + y0), scale, scale), 0)
#----- pygame init
pygame.init()
SCREEN_W, SCREEN_H = 800, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
#---- date init ----
scale = 8
pixel = []
pixel.append('000AA000')
pixel.append('000AA000')
pixel.append('06666660')
pixel.append('60066006')
pixel.append('00666600')
pixel.append('06600660')
pixel.append('66000066')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill( (0, 0, 0) )
    RT_draw(screen, pixel, 0, 0, scale)
    pygame.display.update()
    clock.tick(100)


            
        
              
              
