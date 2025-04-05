#homework n1n2a
n1, n2, a = eval(input('n1, n2, a = '))
cnt = 0
for n in range(n1, n2 + 1):
    if n < 10:
        if n == a:
            cnt += 1
    elif n < 100:
        if n % 10 == a:
            cnt += 1
        if n // 10 == a:
            cnt += 1
    else:
        if n % 10 == a:
            cnt += 1
        if n % 100 // 10 == a:
            
            cnt += 1
        if n // 100 == a:
            cnt += 1
print(cnt)
