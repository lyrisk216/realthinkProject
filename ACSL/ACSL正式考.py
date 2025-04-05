#
topcard = input()
mycard = input()
a = mycard.split(" ")
topcardList = []
topcardList.append(topcard)
stopflag = 0
b = ''
while True:
    for i in range(len(a)):
        flag = 0
        for j in range(3):
            if topcard[j] == a[i][j]:
                flag += 1
        if flag >= 2:
            topcardList.append(a[i])
            topcard = a[i]
            a.pop(i)
            break
        if i == len(a) - 1:
            stopflag = 1
    
    if len(a) == 0:
        break
    if stopflag == 1:
        break
    
for ccc in topcardList:
    b += ccc + ' '
b = b[:-1]
print(b)
            
    


