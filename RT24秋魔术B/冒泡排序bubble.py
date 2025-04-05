#冒泡排序
import random, time

def sort_bubbling(dList):
    for a in range(len(dList) - 1):
        flag = 0
        for i in range(len(dList) - 1 - a):
            if dList[i][0] > dList[i + 1][0]:
                dList[i], dList[i + 1] = dList[i + 1], dList[i]
                flag = 1
        if flag == 0:
            break
    return
def sort_select1(dList):
    nList = [ ]
    length = len(dList)
    for a in range(length):
        iMin = 0
        for i in range(len(dList)):
            if dList[i][0] < dList[iMin][0]:
                iMin = i
        nList.append(dList[iMin])
        dList.pop(iMin)
    return nList
def sort_select2(dList):
    nList = [ ]
    length = len(dList)
    for a in range(length):
        i = dList.index(min(dList))
        nList.append(dList[i])
        dList.pop(i)
    return nList
def insert_one_line(line, dList):
    if len(dList) == 0:
        dList.append(line)
        return
    if line[0] < dList[0][0]:
        dList.insert(0, line)
        return
    if line[0] >= dList[-1][0]:
        dList.append(line)
        return
    bottom, top = 0, len(dList) - 1
    while True:
        i = int((bottom + top) / 2)
        if line[0] < dList[i][0]:
            top = i
        elif line[0] > dList[i][0]:
            bottom = i
        else:
            dList.insert(i, line)
            break
        if bottom + 1 == top:
            dList.insert(top, line)
            break
    return
def sort_insert(dList):
    nList = [ ]
    for line in dList:
        insert_one_line(line, nList)
    return nList
# --- main ---
num = 10000
dList = [ ]
for i in range(num):
    dList.append( [random.random( ), i + 1] )
print('Start')
t0 = time.time()

#sort_bubbling(dList)
nList = sort_insert(dList)
print( time.time() - t0 )
