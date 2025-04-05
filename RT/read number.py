#read number

import pygame, time
def sound_num(s):
    sStr = '零一二三四五六七八九十百千万亿兆京'
    for c in s:
        for i in range(len(sStr)):
            if c == sStr[i]:
                soundList[i].play()
                time.sleep(soundList[i].get_length())
#--- init ----
pygame.mixer.init()
soundList = []
for i in range(11):
    sound = pygame.mixer.Sound(str(i) + ".wav")
    soundList.append(sound)
for s in ('H', 'K', '10K', '100M', 'T', '10KT'):
    sound = pygame.mixer.Sound(s + ".wav")
    soundList.append(sound)
cStr = '零一二三四五六七八九十百千'
while True:
    n = eval(input('n = '))
    word = ''

    n = n % 10000
    if n // 1000 > 0:
        word += cStr[n // 1000] + cStr[12]
        if n % 1000 == 0:
            print(word)
            continue
        if n // 100 % 10 == 0:
            word += cStr[0]
    


    n = n % 1000
    if n // 100 > 0:
        word += cStr[n // 100] + cStr[11]
        if n % 100 == 0:
            print(word)
            continue
        if n // 10 % 10 == 0:
            word += cStr[0]
        
    n = n % 100
    if n <= 10:
        word += cStr[n]
    elif n < 20:
        word += cStr[10] + cStr[n % 10]
    elif n % 10 == 0:
        word += cStr[n // 10] + cStr[10]
    else:
        word += cStr[n//10] + cStr[10] + cStr[n % 10]
    print(word)
