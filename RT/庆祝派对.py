#庆祝派对
nameList = ['Beyonce', 'Taylor', 'Brad', 'Katy',
            'Tom', 'Drake', 'Alicia']
timeList = [ [6, 7], [7, 9], [10, 11], [10, 12],
             [8, 10], [9, 11], [6, 8] ]
tMax, cntMax = 0, 0
for t0 in range(12):
    cnt = 0
    for t in timeList:
        if t[0] <= t0 < t[1]:
            cnt += 1
    if cnt > cntMax:
        tMax, cnt = t0, cnt
print(tMax, cntMax)
