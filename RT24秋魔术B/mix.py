#Mix milk

import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

def dao(tongA, tongB):
    if 0 <= tongA[1] <= (tongB[0] - tongB[1]):
        tongB[1] = tongB[1] + tongA[1]
        tongA[1] = 0
    else:
        temp = tongB[0] - tongB[1]
        tongB[1] += temp
        tongA[1] -= temp
    return tongA, tongB
        
    
    

##[[10, 3], [11, 4], [12, 5]]
#-- main --
tongList = []
for i in range(3):
    tong = input().split()
    tongList.append([int(tong[0]), int(tong[1])])
for i in range(100):
    tongList[i % 3], tongList[(i + 1) % 3] = dao(tongList[i % 3], tongList[(i + 1) % 3])
##    print(tongList)
print(tongList[0][1])
print(tongList[1][1])
print(tongList[2][1])
sys.stdin.close()
sys.stdout.close()
