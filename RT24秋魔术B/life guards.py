#life guards
def get_work_time_by_fire_you(gList, fId):
    bList = [0] * 1000
    for i in range(len(gList)):
        if i == fId:
            continue
        for t in range(gList[i][0], gList[i][1]):
            bList[t] = 1
    return sum(bList)
# --- main ---
guardList = [[5, 9], [1, 4], [3, 7]]
timeMax = 0
for i in range(len(guardList)):
    timeNum = get_work_time_by_fire_you(gList, i)
    if timeNum > timeMax:
        timeMax = timeNum
print(timeMax)
