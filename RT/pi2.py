#pi
import math

n = eval(input('n = '))
nPi1, nPi2 = 1, 1
for n1 in range(10, n + 1):
    p = int(n1 / math.pi)
    for n2 in range(p, p + 2):
        if abs(n1 / n2 - math.pi) < abs(nPi1 / nPi2 - math.pi):
            nPi1, nPi2 = n1, n2


print(nPi1, nPi2, nPi1 / nPi2)
        

        
        
    
