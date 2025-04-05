#ABCD
##cnt = 0
##for a in range(6, 10):
##    for b in range(4, a - 1):
##        for c in range(2, b - 1):
##            for d in range(0, c - 1):
##                print(a, b, c, d)
##                cnt += 1
##print(cnt)
##                    


##cnt = 0
##for a in range(0, 11):
##    for b in range(a + 3, 14):
##        for c in range(b + 3, 17):
##            for d in range(c + 3, 20):
##                for e in range(d + 3, 23):
##                    for f in range(e + 3, 26):
##                        print(chr(a + ord('A')),
##                              chr(b + ord('A')),
##                              chr(c + ord('A')),
##                              chr(d + ord('A')),
##                              chr(e + ord('A')),
##                              chr(f + ord('A')))
##                              
##                        
##                        cnt += 1
##print(cnt)







cnt = 0
pList = [2, 3, 5, 7]
nList = []
for a in range(4):
    for b in range(4):
        if a == b:
            continue
        for c in range(4):
            if a == c or b == c:
                continue
            d = 6 - a - b - c
            nList.append(pList[a] * 1000 + pList[b] * 100 + \
                         pList[c] * 10 +pList[d])
print(nList)
for n1 in range(len(nList) - 1):
    for n2 in range(n1 + 1, len(nList)):
        n = nList[n2] - nList[n1]
        if n ** 0.5 % 1 == 0:
            print(nList[n2], nList[n1], n)
            cnt += 1
print('cnt = ', cnt)





##pList = [2, 3, 5, 7, 11, 13]



   
               
