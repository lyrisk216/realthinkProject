#casino2
import random

numBaozi, numShunzi, numDuizi, numLaji = 0, 0, 0, 0
totalNum = 0
for i in range(1000000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    #排序
    if d3 > d2:
        temp = d2
        d2 = d3
        d3 = temp
    if d2 > d1:
        temp = d1
        d1 = d2
        d2 = temp
    #判断
    if d1 - d2 == 1 and d2 - d3 == 1:
        numShunzi += 1
        continue
    if d1 == d2 and d2 == d3:
        numBaozi += 1
        continue
    elif d1 == d2 or d2 == d3 or d1 == d3:
        numDuizi += 1
    else:
        numLaji += 1

totalNum = numShunzi + numBaozi + numDuizi + numLaji
if totalNum == 1000000:
    print('成功')
    print('豹子', numBaozi, '\t顺子', numShunzi, '\t对子', numDuizi, '\t垃圾', numLaji)
else:
    print('错误')
    print(totalNum)
    print('豹子', numBaozi, '\t顺子', numShunzi, '\t对子', numDuizi, '\t垃圾', numLaji)
        
        
    


    

