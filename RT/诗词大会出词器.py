#诗词大会出词器
import pygame, random, sys
def RT_randtxt( txt ):
    txtList = list( txt )
    rdtxt = ''
    for i in range( len(txt) ):
        r = random.randint( 0, len(txtList) - 1 )
        rdtxt += txtList[r]
        txtList.pop( r )
    return rdtxt
def RT_getwords(poemList):
    if len(poemList) < 2:
        return RT_randtxt('题已出完了不要再搞事')
    r1 = random.randint(0, len(poemList) - 1)
    w1 = poemList[r1]
    poemList.pop(r1)
    r2 = random.randint(0, len(poemList) - 1)
    w2 = poemList[r2]
    poemList.pop(r2)
    return RT_randtxt(w1 + w2)
def RT_jiugong(screen, bgPic, font, word):
    screen.blit( bgPic, ( 0, 0 ) )
    w, h = bgPic.get_size()
    spaceW, spaceH = (w - 1) // 3, (h - 1) // 3
    for i in range(4):
        pygame.draw.line(screen, (0, 0, 0), (0, i * spaceH), (w, i * spaceH), 1)
        pygame.draw.line(screen, (0, 0, 0), (i * spaceW, 0), (i * spaceW, h), 1)
    for i in range(9):
        x, y = i % 3, i // 3
##        img = font.render(word[i], True, (255, 215, 0) )
##        screen.blit(img, (x * spaceW + 8, y * spaceH + 8))
##        
##        img = font.render(word[i], True, (0, 0, 0) )
##        screen.blit(img, (x * spaceW + 5, y * spaceH + 5))
        for a in range(10):
            c = (a * 25, a * 25, a * 25)
            img = font.render(word[i], True, c )
            screen.blit(img, (x * spaceW + a, y * spaceH + a))
#--- main ---
f = open( 'poems.txt', 'r' )
poemList = f.readlines()
f.close( )
for i in range(len(poemList)):
    poemList[i] = poemList[i].strip('\n')
#--- Pygame init ---
pygame.init()
bgPic = pygame.image.load('poetry.jpg')
screen = pygame.display.set_mode( bgPic.get_size() )
clock = pygame.time.Clock()
font = pygame.font.Font('SIMLI.TTF', 150)
screen.blit( bgPic, ( 0, 0 ) )
word = '按任意键开始游戏吧!'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            word = RT_getwords(poemList)
    RT_jiugong(screen, bgPic, font, word)
    pygame.display.update()
    clock.tick(50)
