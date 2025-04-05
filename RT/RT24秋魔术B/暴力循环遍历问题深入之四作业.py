#abcde
pList = [2, 3, 5, 7, 11, 13]
cnt = 0
for i in range(25, 16, -1):
    for p1 in range(3, 6):
        for p2 in range(2, p1):
            if p1 == p2:
                continue
            for p3 in range(1, p2):
                if p1 == p3 or p2 == p3:
                    continue
                for p4 in range(0, p3):
                    if p1 == p4 or p2 == p4 or p3 == p4:
                        continue
                    #print(p1,p2,p3,p4)
                    if pList[p1] + pList[p2] + pList[p3] + pList[p4] == i:
                        cnt += 26 - i
                        print('[',pList[p1],',',pList[p2],',',pList[p3],',',pList[p4],'] = ',i)
                        
print('组数 = ',cnt)                
print('总数 = ', cnt * 4 * 3 * 2 * 1)
             
                
            
