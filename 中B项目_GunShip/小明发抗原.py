#小明发抗原
import math
remainder = 0
n, m, a, b = eval(input('n, m, a, b = '))
total = (n - 1) * m * a
takeNum = b // a * a
runNum = math.ceil(total / takeNum)
#print(total, takeNum, runNum)
for i in range(runNum):
    upFloor = math.ceil(takeNum / (a * m)) 
    remainder = m - ((takeNum / a) % m)
    
