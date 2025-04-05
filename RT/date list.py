#date list
aList = eval(input('a[] = '))
aMax = aList[0]
s = 0
for i in range(len(aList)):
    a = aList[i]
    if aMax < a:
        aMax = a
        print('sum:', s)
        print('avg:', s / len(aList))
        print('max:', aMax)
             
