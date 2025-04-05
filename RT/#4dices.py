#4dices
import random

num = 100000
cnt4, cnt31, cnt22, cnt1234 = 0, 0, 0, 0
for i in range(num):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    if a == b and b == c and a != d:
        cnt31 += 1
    elif a == b and b == d and a != c:
        cnt31 += 1
    elif a == c and c == d and a != b:
        cnt31 += 1
    if a == b and c == d and a != d:
        cnt22 += 1
    elif a == c and b == d and a != d:
        cnt22 += 1
    elif a == d and c == b and a != b:
        cnt22 += 1
    if a == b and b == c and c == d:
        cnt4 += 1
    if a + 1 == b and b + 1 == c and c + 1 == d:
        cnt1234 += 1
    if b + 1 == b and a + 1 == c and c + 1 == d:
        cnt1234 += 1
    if c + 1 == a and a + 1 == b and b + 1 == d:
        cnt1234 += 1
    if d + 1 == a and a + 1 == b and b + 1 == c:
        cnt1234 += 1
    
print(cnt4 / num  * 100, '%')
print(cnt31 / num * 100, '%')
print(cnt22 / num * 100, '%')
print(cnt1234 / num * 100, '%')
    
