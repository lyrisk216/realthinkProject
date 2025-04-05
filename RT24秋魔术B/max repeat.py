#max repeat
word = input('word = ')
word += ' '
lastChr = ''
chrMax, cntMax = '', 0
cnt = 0
for c in word:
    #print('This:', c, '\tLast:', lastChr)
    if c == lastChr:
        cnt +=1
    else:
        if cnt > cntMax:
            chrMax, cntMax = lastChr, cnt
        cnt = 1
    lastChr = c
print(chrMax, cntMax)
