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
#---- date init ----
scale = 4
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
#--------------2---------------
pixelList2 = []
# 第1帧像素数据
pixel = []
pixel.append('................')
pixel.append('........7.7.....')
pixel.append('........777.....')
pixel.append('.......AAAA.....')
pixel.append('......AAAAE.....')
pixel.append('.....AAAAEE.....')
pixel.append('....AAAEEEE.....')
pixel.append('...AAAA.555.....')
pixel.append('....AA.55555E...')
pixel.append('....E55555555...')
pixel.append('.....5..555.....')
pixel.append('.......5555.....')
pixel.append('......555555....')
pixel.append('.....55555555...')
pixel.append('................')
pixel.append('................')
pixelList2.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('........7.7.....')
pixel.append('..A..A..777.....')
pixel.append('.AAA...AAAA.A...')
pixel.append('..A...AAAAE.....')
pixel.append('......AAAEE...A.')
pixel.append('.....AAEEEE.....')
pixel.append('....AAA555...A..')
pixel.append('.A.AAA.555..AAA.')
pixel.append('....A.5555...A..')
pixel.append('.....55555......')
pixel.append('...55555555.....')
pixel.append('....555555...A..')
pixel.append('....4E..E..A....')
pixel.append('........4.......')
pixel.append('................')
pixel.append('................')
pixelList2.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('................')
pixel.append('........7.7.....')
pixel.append('..A..A..777.....')
pixel.append('.AAA...AAAA.A...')
pixel.append('..A...AAAAE.....')
pixel.append('......AAAEE...A.')
pixel.append('.....AAEEEE.....')
pixel.append('....AAA555...A..')
pixel.append('.A.AAA.555..AAA.')
pixel.append('....A.5555...A..')
pixel.append('.....55555......')
pixel.append('...55555555.....')
pixel.append('....555555...A..')
pixel.append('......E.E..A....')
pixel.append('......4.4.......')
pixel.append('................')
pixelList2.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('................')
pixel.append('........7.7.....')
pixel.append('........777...A.')
pixel.append('..A....AAAA.....')
pixel.append('.AAA..AAAAE..A..')
pixel.append('..A..AAAAEE.....')
pixel.append('....AAAEEEE.....')
pixel.append('...AAAA.555.....')
pixel.append('....AA.555555E..')
pixel.append('..A.E5555555....')
pixel.append('.....5..555...A.')
pixel.append('.A.....5555..AAA')
pixel.append('......55555...A.')
pixel.append('.....5555555....')
pixel.append('................')
pixel.append('................')
pixelList2.append(pixel)
#---------3-----------
pixelList3 = []
# 第1帧像素数据
pixel = []
pixel.append('................')
pixel.append('................')
pixel.append('................')
pixel.append('......222......6')
pixel.append('......336.....6.')
pixel.append('......333....6..')
pixel.append('..444344....4...')
pixel.append('.4433.333..4....')
pixel.append('4433433..33.....')
pixel.append('4444411..4......')
pixel.append('..4441114.......')
pixel.append('..6611.11.......')
pixel.append('.......11.......')
pixel.append('.......66.......')
pixel.append('................')
pixel.append('................')
pixelList3.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('................')
pixel.append('................')
pixel.append('................')
pixel.append('......222.......')
pixel.append('......336......6')
pixel.append('......333.....6.')
pixel.append('.....444.....6..')
pixel.append('...44333....4...')
pixel.append('..4433333..4....')
pixel.append('.4443311.33.....')
pixel.append('.444441114......')
pixel.append('.....1111.......')
pixel.append('....611.........')
pixel.append('.....66.........')
pixel.append('................')
pixel.append('................')
pixelList3.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('................')
pixel.append('................')
pixel.append('..............6.')
pixel.append('......222....6..')
pixel.append('......336...6...')
pixel.append('......333..4....')
pixel.append('....4444..4.....')
pixel.append('..443333.3......')
pixel.append('.443343333......')
pixel.append('.4444433........')
pixel.append('444441111.......')
pixel.append('.44411..11......')
pixel.append('...11...66......')
pixel.append('...66...........')
pixel.append('................')
pixel.append('................')
pixelList3.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('................')
pixel.append('................')
pixel.append('................')
pixel.append('......222.....6.')
pixel.append('......336....6..')
pixel.append('......333...6...')
pixel.append('...44344...4....')
pixel.append('..4334333.4.....')
pixel.append('.4334433.33.....')
pixel.append('4444411.4.......')
pixel.append('444441111.......')
pixel.append('...661..11......')
pixel.append('.........66.....')
pixel.append('................')
pixel.append('................')
pixel.append('................')
pixelList3.append(pixel)



x, y = 0, 0
spdX, spdY = 2.5, 1
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spdX = -1
            if event.key == pygame.K_RIGHT:
                spdX = 1
            if event.key == pygame.K_UP:
                spdY = -1
            if event.key == pygame.K_DOWN:
                spdY = 1
    i += 1
    x += spdX
    y += spdY
    if x < 0 or x > SCREEN_W:
        spdX *= -1
    if y < 0 or y > SCREEN_H:
        spdY *= -1
    #screen.fill( (0, 0, 0) )
    RT_draw(screen, pixelList[i // 6 % 4], x, y, scale)
    RT_draw(screen, pixelList2[i // 6 % 4], x + 16 * scale, y, scale)
    RT_draw(screen, pixelList3[i // 6 % 4], x + 32 * scale, y, scale)

    pygame.display.update()
    clock.tick(200)


            
        
              
              
