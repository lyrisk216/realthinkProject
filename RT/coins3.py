import random

num = 100000
cnt = 0
for i in range(num):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    if b + 1 == a == c - 1:
        cnt += 1
    if c + 1 == a == b - 1:
        cnt += 1
    if a + 1 == b == c - 1:
        cnt += 1
    if c + 1 == b == a - 1:
        cnt += 1
    if a + 1 == c == b - 1:
        cnt += 1
    if b + 1 == c == a - 1:
        cnt += 1
print(cnt / num * 100, '%')
        
    
