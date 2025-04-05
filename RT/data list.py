#data list
aList = eval(input('a[] = '))
aMax, aMaxId = aList[0], 0
aMin, aMinId = aList[0], 0
sumEven = 0
sumOdd = 0
s = 0
length = len(aList)
for i in range(len(aList)):
    a = aList[i]
    s += a
    if aMax < a:
        aMax, aMaxId = a, i
    if aMin > a:
        aMin, aMinId = a, i
    if i % 2 == 0:
        sumOdd += a
    else:
        sumEven += a
print('sum = ', s)
print('avg = ', s / len(aList))
print('avgOdd = ', sumOdd / ((length // 2) + (length % 2)))
print('avgEven = ', sumEven / (length // 2))
if len(aList) % 2 == 1:
    print('max = ', aMax, '\tNo.', aMaxId + 1)
else:
    print('min = ', aMin, '\tNo.', aMinId + 1)
