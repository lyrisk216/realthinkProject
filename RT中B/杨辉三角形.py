#杨辉三角形

n = eval(input('n = '))
##for y in range(n):
yhList = [0] * n 
yhList[0] = 1
print(yhList)
#----main----
##多项式法
##for y in range(n - 1):
##
##    newLine = yhList[y][:]
##    newLine.insert(0, 0)
##    for x in range(n):
##        yhList[y + 1][x] = yhList[y][x] + newLine[x]
##        

###累加法
##for y in range(n - 1):
##    yhList[y + 1][0] = 1
##    for x in range(1, n):
##        yhList[y + 1][x] = yhList[y][x] + yhList[y][x - 1]
##
##
##for y in range(n - 1):
##    yhList[y][0] = 1
##    for x in range(n):
##        
##

for y in range(n - 1):
    newLine = yhList[:]
    newLine.insert(0, 0)
    for x in range(n):
        yhList[x] = yhList[x] + newLine[x]
    print(yhList)
#----output----
##for line in yhList:
##    print(line)

