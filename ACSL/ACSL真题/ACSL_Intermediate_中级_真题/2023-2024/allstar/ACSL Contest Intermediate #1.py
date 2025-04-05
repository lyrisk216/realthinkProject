# ACSL All-Star Test1


def horizontal(newGrid, numGrid, word, n, m):
    if len(word) > m:
        return numGrid, 0
    for i in range(n):
        for j in range(m - len(word) + 1):
            wordStat = 0
            for k in range(len(word)):
                if word[k] != newGrid[i * m + j + k]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[i * m + j + k] = 1
                return numGrid, 1
            wordStat = 0
            for k in range(len(word)):
                if word[len(word) - k - 1] != newGrid[i * m + j + k]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[i * m + j + k] = 1
                return numGrid, 1
    return numGrid, 0


def vertical(newGrid, numGrid, word, n, m):
    if len(word) > n:
        return numGrid, 0
    for i in range(m):
        for j in range(n - len(word) + 1):
            wordStat = 0
            for k in range(len(word)):
                if word[k] != newGrid[(j + k) * m + i]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[(j + k) * m + i] = 1
                return numGrid, 1
            wordStat = 0
            for k in range(len(word)):
                if word[len(word) - k - 1] != newGrid[(j + k) * m + i]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[(j + k) * m + i] = 1
                return numGrid, 1
    return numGrid, 0


def diagonal(newGrid, numGrid, word, n, m):
    for i in range(n - len(word) + 1):
        for j in range(m - len(word) + 1):
            wordStat = 0
            for k in range(len(word)):
                if word[k] != newGrid[(i + k) * m + j + k]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[(i + k) * m + j + k] = 1
                return numGrid, 1
            wordStat = 0
            for k in range(len(word)):
                if word[len(word) - k - 1] != newGrid[(i + k) * m + j + k]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[(i + k) * m + j + k] = 1
                return numGrid, 1
            wordStat = 0
            for k in range(len(word)):
                if word[k] != newGrid[(i + k) * m + j + len(word) - k - 1]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[(i + k) * m + j + len(word) - k - 1] = 1
                return numGrid, 1
            wordStat = 0
            for k in range(len(word)):
                if word[len(word) - k - 1] != newGrid[(i + k) * m + j + len(word) - k - 1]:
                    wordStat = 1
                    break
            if wordStat == 0:
                for k in range(len(word)):
                    numGrid[(i + k) * m + j + len(word) - k - 1] = 1
                return numGrid, 1
    return numGrid, 0

def find(newGrid, numGrid, word, n, m):
    numGrid, stat = horizontal(newGrid, numGrid, word, n, m)
    if stat == 1:
        return numGrid
    numGrid, stat = vertical(newGrid, numGrid, word, n, m)
    if stat == 1:
        return numGrid
    numGrid, stat = diagonal(newGrid, numGrid, word, n, m)
    return numGrid


# ----- main -----
n, m = input().split()
n, m = eval(n), eval(m)
newGrid, numGrid = [], []
enterStr = input()
wordList = list(input().split())
for i in enterStr:
    newGrid.append(i)
numGrid = [0] * (n * m)
for word in wordList:
    numGrid = find(newGrid, numGrid, word, n, m)
resStr = ""
for i in range(n * m):
    if numGrid[i] == 0:
        resStr += newGrid[i]
print(resStr)
