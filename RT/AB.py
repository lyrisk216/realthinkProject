def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
#--- main ---
a, b = eval(input('a, b = '))
flag = True
pList = []
n = a
for i in range(a, b + 1):
    if is_prime(i):
        pList.append(i)
#print(pList)
pMax1, pMax2 = 2, 3
for i in range(len(pList) - 1):
    if pList[i + 1] - pList[i] > pMax2 - pMax1:
         pMax1, pMax2 = pList[i], pList[i + 1] 
print(pMax1, pMax2)   
