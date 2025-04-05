# ACSL All-Star Test2

cards = "3456789TJQKA2"


def count_cards(pStr):
    numStr = "0000000000000"
    for i in pStr:
        numStr = numStr[:cards.find(i)] + str(eval(numStr[cards.find(i)]) + 1) + numStr[(cards.find(i) + 1):]
    return numStr


def find_max(nStr):
    maxCnt, maxInd = 0, 0
    for i in range(len(nStr)):
        if eval(nStr[i]) > maxCnt:
            maxCnt = eval(nStr[i])
            maxInd = i
    return maxCnt, maxInd


def find_deal(nStr, nowLen, cardId):
    for i in range(len(nStr)):
        if eval(nStr[i]) == nowLen:
            if i > cardId:
                return i
    return -1


# ----- main -----
n = eval(input())
total = []
pCount = []
for i in range(n):
    nStr = ""
    kList = list(input().split())
    for j in kList:
        nStr += j[:1]
    total.append(nStr)
    numStr = count_cards(nStr)
    pCount.append(numStr)
pList = []
turn = 0
nowLen = 0
bidder = 0
cardId = 0
times = 0
while len(pList) < (n - 1):
    if turn == bidder:
        times += 1
    if (turn + 1) in pList:
        turn = (turn + 1) % n
        continue
    print(pCount[turn])
    print(cards[cardId], nowLen)
    if nowLen == 0:
        times = 0
        nowLen, cardId = find_max(pCount[turn])
        bidder = turn
        playerStr = pCount[turn]
        playerStr = playerStr[:cardId] + str(eval(playerStr[cardId]) - nowLen) + playerStr[(cardId + 1):]
        pCount[turn] = playerStr
        if playerStr == "0000000000000":
            pList.append(turn + 1)
        turn = (turn + 1) % n
        continue
    else:
        if turn == bidder:
            times = 0
            newId = find_deal(pCount[turn], nowLen, cardId)
            if newId == -1:
                nowLen = 0
                continue
            cardId = newId
            playerStr = pCount[turn]
            playerStr = playerStr[:cardId] + str(eval(playerStr[cardId]) - nowLen) + playerStr[(cardId + 1):]
            pCount[turn] = playerStr
            if playerStr == "0000000000000":
                pList.append(turn + 1)
            turn = (turn + 1) % n
            continue
        elif times != 0:
            bidder = turn
            times = 0
            continue
        else:
            newId = find_deal(pCount[turn], nowLen, cardId)
            if newId == -1:
                turn = (turn + 1) % n
                continue
            times = 0
            cardId = newId
            bidder = turn
            playerStr = pCount[turn]
            playerStr = playerStr[:cardId] + str(eval(playerStr[cardId]) - nowLen) + playerStr[(cardId + 1):]
            pCount[turn] = playerStr
            if playerStr == "0000000000000":
                pList.append(turn + 1)
            turn = (turn + 1) % n
            continue

nSum = round(n * (n + 1) / 2)
for k in pList:
    nSum -= k
roadStr = ""
for k in pList:
    roadStr += str(k)
    roadStr += " "
roadStr += str(nSum)
print(roadStr)
