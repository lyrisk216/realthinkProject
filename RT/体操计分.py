#RT Lesson 体操计分

s = 0

avg = 0

scList = [9.8, 9.2, 9.5, 10, 9.4, 10, 9.3, 9.7]
cntMin = 0
sMax = scList[0]
sMin = scList[0]
for i in range(len(scList)):
    sc = scList[i]
    s += sc
    if sMax < sc:
        sMax = sc
    if sMin > sc:
        sMin = sc
        cntMin = i + 1
    print(sc)

print('Max = ', sMax)
print('Min = ', sMin)
print('avg = ', (s - sMax - sMin) / ((len(scList) - 2)))
print('cntMin = ', cntMin)
