#prime number filter
import time

n = eval(input('n = '))
t0 = time.time()
'''
pList = [True] * (n + 1)
pList[0], pList[1] = False, False
for w in range(2, int(n ** 0.5) + 1):
    if pList[w]:
        for p in range(w * w, n + 1, w):
            pList[p] = False
'''
pList = [False, False, True] + [True, False] * (n // 2 - 1)
for w in range(3, int(n ** 0.5) + 1, 2):
    if pList[w]:
        for p in range(w * w, n + 1, 2 * w):
            pList[p] = False
print('time = ', time.time() - t0)
print(sum(pList))
