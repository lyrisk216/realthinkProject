def cap(c):
    if 'a'<= c <= 'z':
        return chr(ord(c) - 32)
    else:
        return c
def count_chr(txt, c0):
    cnt = 0
    for c in txt:
        if cap(c) == cap(c0):
            cnt += 1
    return cnt
#--- main ---
txt = '''The quick brown fox, named Roxanne, jumped over Bruno, a lazydog.'''
cList, cntList = [], []
cntYuan = 0
cntBig = 0
wList = []
word = ''
for i in range(26):
    c = chr(i + ord('A'))
    cList.append(c)
    cnt = count_chr(txt, c)
    cntList.append(cnt)
    if c == chr(ord('A')) or c == chr(ord('O')) or c == chr(ord('E')) or c == chr(ord('U')):
        cntYuan += cnt
    if 'A' <= c <= 'Z':
        cntBig += 1
    print(c, '有', cnt, '个')
    
print('元音:', cntYuan, '大写:', cntBig)

for a in range(len(cntList)- 1):
    flag = 0
    for i in range(len(cntList) - 1 - a):
        if cntList[i] < cntList[i + 1]:
            cntList[i], cntList[i + 1] = cntList[i + 1], cntList[i]
            cList[i], cList[i + 1] = cList[i + 1], cList[i]
            flag = 1
    if flag == 0:
        break
    

print('出现最频繁的字母是:', cList[0], '出现了', cntList[0], '次')
for c in txt:
    if 'A' <= c <= 'z' or 'a' <= c <= 'z':
        word += c
    elif word != '':
        wList.append(word)
        word = ''
print(wList)

for a in range(len(wList)- 1):
    flag = 0
    for i in range(len(wList) - 1 - a):
        #从大到小排序，判断顺序是否正确
        if len(wList[i]) < len(wList[i + 1]):
            wList[i], wList[i + 1] = wList[i + 1], wList[i]
            flag = 1
    if flag == 0:
        break
print(wList)

wordMax = ''
for w in wList:
    if len(w) > len(wordMax):
        wordMax = w
print(wordMax)
for a in range(len(wList)- 1):
    flag = 0
    for i in range(len(wList) - 1 - a):
        #从大到小排序，判断顺序是否正确
        if len(wList[i]) == len(wList[i + 1]) and wList[i][0] < wList[i + 1][0]:
            wList[i], wList[i + 1] = wList[i + 1], wList[i] 
            flag = 1
    if flag == 0:
        break
print(wList)  
             

##for i in range(len(wList) - 1):
##    if len(wList[i]) > len(wList[i + 1]):
##        wList[i], wList[i + 1] = wList[i + 1], wList[i]
  


