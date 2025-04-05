#RealThink lessson 键盘电子琴 piano
import pygame, sys
def get_key_index(key, kList):
    for i in range(len(kList)):
        if key == ord(kList[i]):
            return i
    return -1
#------ Pygame init -------
pygame.init()
pianoImg = pygame.image.load('piano.bmp')
screen = pygame.display.set_mode( pianoImg.get_size() )
pygame.display.set_caption('RT-PIANO')
#----date init -----
noteImg = pygame.image.load('note.bmp')
keyList = 'zxcvbnm' + 'qwertyu' + '1234567' + 'sdghj'
soundList = []
for noteLevel in '345':
    for noteName in 'cdefgab':
        oggSound = pygame.mixer .Sound(noteName + noteLevel + '.ogg')
        soundList.append(oggSound)
for noteLevel in '3':
    for noteName in'cdfga':
        oggSound = pygame.mixer .Sound(noteName + noteLevel + 'm.ogg')
        soundList.append(oggSound)
keyFlagList = [0] * len(keyList)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            i = get_key_index(event.key, keyList)
            if i >= 0:
                soundList[i].play()
                keyFlagList[i] = 1
        elif event.type == pygame.KEYUP:
            i = get_key_index(event.key, keyList)
            if i >= 0:
                keyFlagList[i] = 0
    screen.blit(pianoImg, (0, 0))
    for i in range(len(keyFlagList)):
        if keyFlagList[i]:
            screen.blit(noteImg, (i * 30 + 2, 80))
    pygame.display.update()                









                
        
