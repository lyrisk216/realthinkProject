#RT RPG

import pygame, sys

def RT_draw(screen, pixel, x0, y0, scale):
    color = ( pygame.color.THECOLORS['black'],
              pygame.color.THECOLORS['gray32'],
              pygame.color.THECOLORS['gray64'],
              pygame.color.THECOLORS['white'],
              pygame.color.THECOLORS['red'],
              pygame.color.THECOLORS['blue'],
              pygame.color.THECOLORS['orange'],
              pygame.color.THECOLORS['orange'],
              pygame.color.THECOLORS['brown'],
              pygame.color.THECOLORS['purple'],
              pygame.color.THECOLORS['yellow'],
              pygame.color.THECOLORS['cyan'],
              pygame.color.THECOLORS['sienna'],
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
#----- data init -----
scale = 8
pixelList = []
# 第1帧像素数据
pixel = []
pixel.append('.......2........')
pixel.append('......2222......')
pixel.append('......2322......')
pixel.append('.....223322.....')
pixel.append('......333.......')
pixel.append('.......3........')
pixel.append('......3..3.3....')
pixel.append('....3.3..3.3....')
pixel.append('...3..3..3.3....')
pixel.append('......3..3.3....')
pixel.append('..7771222213....')
pixel.append('.7777.3..3......')
pixel.append('.7777.3..3......')
pixel.append('..77..3..3......')
pixel.append('......3..3......')
pixel.append('................')
pixelList.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('................')
pixel.append('.......222......')
pixel.append('......22322.....')
pixel.append('......223322....')
pixel.append('......2333......')
pixel.append('........3.......')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3..3...')
pixel.append('....3222121.....')
pixel.append('......32233.....')
pixel.append('.....3777..3....')
pixel.append('....3.7777..3...')
pixel.append('......777...3...')
pixel.append('................')
pixelList.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('................')
pixel.append('.......222......')
pixel.append('......22322.....')
pixel.append('......223322....')
pixel.append('......2333......')
pixel.append('........3.......')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3..3...')
pixel.append('....322222...3..')
pixel.append('.....33.337.....')
pixel.append('....3..7737.....')
pixel.append('...3...77737....')
pixel.append('........773.....')
pixel.append('................')
pixelList.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('................')
pixel.append('.......222......')
pixel.append('......22322.....')
pixel.append('......223322....')
pixel.append('......2333......')
pixel.append('........3.......')
pixel.append('....3.3..3.3....')
pixel.append('....3.3..3.3....')
pixel.append('......3..3.3....')
pixel.append('...3.33..2..3...')
pixel.append('...33222222.77..')
pixel.append('......3.33.777..')
pixel.append('.....3...3.7777.')
pixel.append('...3......3.777.')
pixel.append('..........3.....')
pixel.append('................')
pixelList.append(pixel)




x, y = 0, 0
spdX, spdY = 3, 1.2
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    i += 1
    x += spdX
    y += spdY
    if x < 0 or x > SCREEN_W:
        spdX *= -1
    if y < 0 or y > SCREEN_H:
        spdY *= -1
    screen.fill( (0, 0, 0) )
    RT_draw(screen, pixelList[i // 4 % 4], x, y, scale)
    pygame.display.update()
    clock.tick(100)


                                 
                                 
                                 
                                 
                                 
                            
                                 
                
              
              
              
            
              
