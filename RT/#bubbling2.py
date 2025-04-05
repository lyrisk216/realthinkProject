#bubbling2
nList = list(eval(input('n[] = ')))
aList = []
for i in range(len(nList)):
    aList.append(i + 1)
print(nList)
print(aList)
for a in range(len(nList)- 1):
    flag = 0
    for i in range(len(nList) - 1 - a):
        #从大到小排序，判断顺序是否正确
        if nList[i] < nList[i + 1]:
            nList[i], nList[i + 1] = nList[i + 1], nList[i]
            aList[i], aList[i + 1] = aList[i + 1], aList[i]
            flag = 1
    print(nList)
    print(aList)
    if flag == 0:
        break
print()
print(nList)
print(aList)

