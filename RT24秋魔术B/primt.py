#prime neighbours
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x / 2) + 1, 2):
        if x % i == 0:
            return False
    return True
# --- main ---
pList = [0] * 101
for i in range(100):
    if is_prime(i):
        pList[i] = 1
print(pList)
nList = eval(input('nList = '))
dList = []
for i in range(len(nList) - 1):
    dList.append(abs(nList[i + 1 ] - nList[i]))
print(dList)
output = 'good'
for d in dList:
    if pList[d] == 0:
        output = 'bad'
        break
    elif pList[d] == 1:
        pList[d] += 1
    elif pList[d] == 2:
        output = 'bad'
        break
print(output)
