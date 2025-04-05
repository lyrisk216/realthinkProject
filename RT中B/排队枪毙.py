#排队
##qList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
##p = 0
##for i in range(len(qList) - 1):
##    p = (p + 4) % len(qList)
##    print(qList[p])
##    print(qList.pop(p))
##print(qList)    
qList = [1] * 16
p = -1
for i in range(len(qList) - 1):     #要删除15个数
    for a in range(5):              #每次有效走5步
        while True:                 #每次有效走1步
            p += 1
            p = p % len(qList)
            if qList[p] == 0:
               continue
            break
    print(qList[p])
    qList[p] = 0

while True:
    if qList[p] == 1:
        break
    else:
        p += 1
        p = p % len(qList)
        
print('最后活下来的是', p + 1, '号')

