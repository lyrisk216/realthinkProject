#地铁四号线票价计算 V0.9
def cap(word):
    word2 = ''
    for c in word:
        if 'a' <= c <= 'z':
            word2 += chr(ord(c) - 32)
        else:
            word2 += c
    return word2
def station_input(info, sDict):
    while True:
        word = cap(input(info))
        try:
            i = sDict[word]
        except:
            print('Not exist!')
            continue
        return i
#----main----
f = open('metro4.in', 'r')
lineList = f.readlines()
f.close()
stationList = []
for line in lineList:

    stationList.append(line.split())
print(stationList)

stationDict = {}
for i in range(len(stationList)):
    stationDict[stationList[i][0]] = i
    stationDict[cap(stationList[i][1])] = i
while True:
    stationId1 = station_input('Station1 name:', stationDict)
    stationId2 = station_input('Station2 name:', stationDict)
    print('From:', stationList[stationId1], stationId1)
    print('To:', stationList[stationId2], stationId2)
    stA, stB = stationId1, stationId1
    length = 0
    while True:
        length += 1
        stA = (stA + 1) % len(stationList)
        stB = (stB - 1) % len(stationList)
        print('A:', stationList[stA][0], '\tB:', stationList[stB][0])
        flag = ''
        if stA == stationId2:
            flag = 'A'
        if stB == stationId2:
            flag = 'B'
        if flag != '':
            print('plan' + flag + 'is better.\t', length, 'stations',
                  '\tamount:', length // 4 + 3)
            f = open('metro4.in', 'w')
            f.write(str(length) + ' ' + str(length // 4 + 3))
            f.close()
            break
