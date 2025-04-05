#4coins
import random

num = 100000
cnt4, cnt31, cnt22, cnt1234, cntFalse = 0, 0, 0, 0, 0
for i in range(num):
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    c = random.randint(0, 1)
    d = random.randint(0, 1)
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
    if b + 1 == b and a + 1 == c and c + 1 == d:
        cnt1234 += 1
    if c + 1 == a and a + 1 == b and b + 1 == d:
        cnt1234 += 1
    if d + 1 == a and a + 1 == b and b + 1 == c:
        cnt1234 += 1
    
print('4:', cnt4 / num * 100, '%')
print('31:', cnt31 / num * 100, '%')
print('22:', cnt22 / num * 100, '%')
print('1234:', cnt1234 / num * 100, '%')
print('False:', num - (cnt4 + cnt31 + cnt22), '%')
      

    
    
