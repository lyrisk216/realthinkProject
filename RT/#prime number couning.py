#prime number counting
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
#-----main-----
num = eval(input('num = '))
t0 = time.time()
cnt = 0
for i in range(num + 1):
    if is_prime(i):
        #print(i, end = '\t')
        cnt += 1
print('time = ', time.time() - t0)
print('cnt = ', cnt)
