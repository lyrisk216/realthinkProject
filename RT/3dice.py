#3dice
import random

num = 100000
cnt123 = 0
for i in range(num):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    if a + 1 == b and b + 1 == c:
        cnt123 += 1
    if b + 1 == a and a + 1 == c:
        cnt123 += 1
    if c + 1 == a and a + 1 == b:
        cnt123 += 1
print('123:', cnt123 / num * 100, '%')
