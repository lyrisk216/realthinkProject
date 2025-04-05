#4dices
import random

num = 100000
cnt4, cnt31, cnt22, cnt1234, cnt1235 = 0, 0, 0, 0, 0
for i in range(num):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    if a == b and b == c and a != d:
        cnt31 += 1
    if a == b and b == d and a != c:
        cnt31 += 1
    if a == c and c == d and a != b:
        cnt31 += 1
    if b == c and c == d and b != a:
        cnt31 += 1
    if a == b and c == d and a != d:
        cnt22 += 1
    if a == c and b == d and a != d:
        cnt22 += 1
    if a == d and c == b and a != b:
        cnt22 += 1
    if a == b and b == c and c == d:
        cnt4 += 1
    if a + 1 == b and b + 1 == c and c + 1 == d:
        cnt1234 += 1
    if 
    if b + 1 == a and a + 1 == c and c + 1 == d:
        cnt1234 += 1
    if c + 1 == a and a + 1 == b and b + 1 == d:
        cnt1234 += 1
    if d + 1 == a and a + 1 == b and b + 1 == c:
        cnt1234 += 1

    if a + 1 == b and b + 1 == c and a != d and b != d and c != d and c + 1 != d and a - 1 != d: 
        cnt1235 += 1
    if a + 1 == b and b + 1 == d and a != c and b != c and d != c and d + 1 != c and a - 1 != c: 
        cnt1235 += 1
    if a + 1 == c and c + 1 == b and a != d and b != d and c != d and b + 1 != d and a - 1 != d:
        cnt1235 += 1
    if a + 1 == c and c + 1 == d and a != b and c != b and d != b and d + 1 != b and a - 1 != b:
        cnt1235 += 1
    if a + 1 == d and d + 1 == b and a != c and b != c and d != c and b + 1 != c and a - 1 != c:
        cnt1235 += 1
    if a + 1 == d and d + 1 == c and a != b and c != b and d != b and c + 1 != b and a - 1 != b:
        cnt1235 += 1

    if b + 1 == a and a + 1 == c and a != d and b != d and c != d and c + 1 != d and b - 1 != d:
        cnt1235 += 1
    if b + 1 == a and a + 1 == d and a != c and b != c and d != c and d + 1 != c and b - 1 != c:
        cnt1235 += 1
    if b + 1 == c and c + 1 == a and a != d and b != d and c != d and a + 1 != d and b - 1 != d:
        cnt1235 += 1
    if b + 1 == c and c + 1 == d and b != a and c != a and d != a and d + 1 != a and b - 1 != a:
        cnt1235 += 1
    if b + 1 == d and d + 1 == a and a != c and b != c and d != c and a + 1 != c and b - 1 != c:
        cnt1235 += 1
    if b + 1 == d and d + 1 == c and b != a and c != a and d != a and c + 1 != a and b - 1 != a:
        cnt1235 += 1

    if c + 1 == a and a + 1 == b and a != d and b != d and c != d and b + 1 != d and c - 1 != d:
        cnt1235 += 1
    if c + 1 == a and a + 1 == d and a != b and c != b and d != b and d + 1 != b and c - 1 != b:
        cnt1235 += 1
    if c + 1 == b and b + 1 == a and a != d and b != d and c != d and a + 1 != d and c - 1 != d:
        cnt1235 += 1
    if c + 1 == b and b + 1 == d and b != a and c != a and d != a and b + 1 != a and c - 1 != a:
        cnt1235 += 1
    if c + 1 == d and d + 1 == b and b != a and c != a and d != a and b + 1 != a and c - 1 != a:
        cnt1235 += 1
    if c + 1 == d and d + 1 == a and a != b and c != b and d != b and a + 1 != b and c - 1 != b:
        cnt1235 += 1

    if d + 1 == a and a + 1 == b and a != c and b != c and d != c and b + 1 != c and d - 1 != c:
        cnt1235 += 1
    if d + 1 == a and a + 1 == c and a != b and c != b and d != b and c + 1 != b and d - 1 != b:
        cnt1235 += 1
    if d + 1 == b and b + 1 == a and a != c and b != c and d != c and a + 1 != c and d - 1 != c:
        cnt1235 += 1
    if d + 1 == b and b + 1 == c and b != a and c != a and d != a and c + 1 != a and d - 1 != a:
        cnt1235 += 1
    if d + 1 == c and c + 1 == a and a != b and c != b and d != b and a + 1 != b and d - 1 != b:
        cnt1235 += 1
    if d + 1 == c and c + 1 == b and b != a and c != a and d != a and b + 1 != a and d - 1 != a:
        cnt1235 += 1

        
print('4:', cnt4 / num  * 100, '%')
print('31:', cnt31 / num * 100, '%')
print('22:', cnt22 / num * 100, '%')
print('1234:', cnt1234 / num * 100, '%')
print('1235:', cnt1235 / num * 100, '%')
    
