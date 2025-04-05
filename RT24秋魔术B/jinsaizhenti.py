#USACO lifeguards_bronze_jan18

import sys
sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

def get_work_time_by_fire_you(gList, fId):
    bList = [0] * 1000
    for i in range(len(gList)):
        #print('loop ', i, ',', fId)
        if i == fId:
            continue
        for t in range(gList[i][0], gList[i][1]):
            bList[t] = 1
    return sum(bList)
#-- main --
#guardList = [[5, 9], [1, 4], [3, 7]]
n = int(input())
guardList = []
for i in range(n):
    guard = input().split()
    guardList.append([int(guard[0]), int(guard[1])])
    #print("append: ", guard[0], guard[1])

timeMax = 0
for i in range(len(guardList)):
    timeNum = get_work_time_by_fire_you(guardList, i)
    #print(timeNum)
    if timeNum > timeMax:
        timeMax = timeNum
print(timeMax)

sys.stdin.close()
sys.stdout.close()
