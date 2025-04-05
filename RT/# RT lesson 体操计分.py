#体操计分

s = 0
sMax = 0
sMin = 10
pMin = 0
scList = [9.8, 9.2, 9.5, 10, 9.4, 10, 9.3, 9.7]
sMax = scList[0]
sMin = scList[0]
for i in range(len(scList)):
    sc = scList[i]
    s += sc
    if sMax < sc:
        sMax = sc
    if sMin > sc:
        sMin = sc
        pMin = i
    print(sc)
print('max = ', sMax)
print('min = ', sMin)
print('avg = ', s / len(scList))
avg2 = ((s - sMax -sMin) /  (len(scList) - 2))
print('avg2 = ', avg2)
print('refNum = ', pMin)




    
    
