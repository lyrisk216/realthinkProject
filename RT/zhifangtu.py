#prime number counting
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True
#----main----
n = eval(input('n = '))
cnt = 0
step = 100
for j in range((n + step - 1) // step):
    for i in range(1 + (j * step), (step + 1) + (j * step), 1):
        if is_prime(i):
            cnt += 1
    print('cnt = ', cnt)
    for a in range(cnt):
        print('*', end = ' ')
    print('\t')
    cnt = 0
