#hanxin
n = 0
cnt = 0

while True:
    n += 1
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        print(n)
        break

for n in range(1000, 0, -1):
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        print(n)
        break
for n in range(1000, 0, -1):
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        cnt += 1
print(cnt)
n, cnt = 0, 0
while cnt < 12:
    n += 1
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        print(n)
        cnt += 1
        if cnt == 12:
            break


    
