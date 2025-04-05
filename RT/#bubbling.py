#bubbling1
nList = list(eval(input('nList = ')))
mList = []
print('nList = ', nList)
print('mList = ', mList)
for i in range(len(nList)):
    mList.append(i + 1)
for a in range(len(nList) - 1):
    flag = 0
    for i in range(len(nList) - a - 1):
        if nList[i] < nList[i + 1]:
            nList[i], nList[i + 1] = nList[i + 1], nList[i]
            mList[i], mList[i + 1] = mList[i + 1], mList[i]
            flag = 1
    print('nList = ', nList)
    print('mList = ', mList)
    if flag == 0:
        break
print()
print('nList = ', nList)
print('mList = ', mList)
