#casino4
import random

def is3same(a, b, c):
    if b + 1 == a == c - 1:
        return True
    if c + 1 == a == b - 1:
        return True
    if a + 1 == b == c - 1:
        return True
    if c + 1 == b == a - 1:
        return True
    if a + 1 == c == b - 1:
        return True
    if b + 1 == c == a - 1:
        return True
    return False
#----------main----------
num = 100000
cnt = 0
for i in range(num):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    flag4 = 0
    if a + 3 == b + 2 == c + 1 == d:
        flag4 += 1
    if a + 3 == b + 2 == d + 1 == c:
        flag4 += 1
    if a + 3 == c + 2 == b + 1 == d:
        flag4 += 1
    if a + 3 == c + 2 == d + 1 == b:
        flag4 += 1
    if a + 3 == d + 2 == b + 1 == c:
        flag4 += 1
    if a + 3 == d + 2 == c + 1 == b:
        flag4 += 1

    if b + 3 == a + 2 == c + 1 == d:
        flag4 += 1
    if b + 3 == a + 2 == d + 1 == c:
        flag4 += 1
    if b + 3 == c + 2 == a + 1 == d:
        flag4 += 1
    if b + 3 == c + 2 == d + 1 == a:
        flag4 += 1
    if b + 3 == d + 2 == a + 1 == c:
        flag4 += 1
    if b + 3 == d + 2 == c + 1 == a:
        flag4 += 1

    if c + 3 == b + 2 == a + 1 == d:
        flag4 += 1
    if c + 3 == b + 2 == d + 1 == a:
        flag4 += 1
    if c + 3 == a + 2 == b + 1 == d:
        flag4 += 1
    if c + 3 == a + 2 == d + 1 == b:
        flag4 += 1
    if c + 3 == d + 2 == b + 1 == a:
        flag4 += 1
    if c + 3 == d + 2 == a + 1 == b:
        flag4 += 1

    if d + 3 == b + 2 == c + 1 == a:
        flag4 += 1
    if d + 3 == b + 2 == a + 1 == c:
        flag4 += 1
    if d + 3 == c + 2 == b + 1 == a:
        flag4 += 1
    if d + 3 == c + 2 == a + 1 == b:
        flag4 += 1
    if d + 3 == a + 2 == b + 1 == c:
        flag4 += 1
    if d + 3 == a + 2 == c + 1 == b:
        flag4 += 1

    if flag4 == 0:
        if is3same(a, b, c) or \
           is3same(a, b, d) or \
           is3same(a, c, d) or \
           is3same(b, c, d):
            cnt += 1
        

print(cnt / num * 100, '%')


    

    
    
    
    
