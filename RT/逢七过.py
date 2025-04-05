#逢七过
def have7(n):
    if n % 7 == 0:
        return True
    while n > 0:
        if n % 10 == 7:
            return True
        n //= 10
    return False
#-----main-----
a, b = eval(input('a, b = '))
cnt = 0
for i in range(a, b + 1):
    if '7' in str(i) or i % 7 == 0:
        print('pass')
        cnt += 1
    else:
        print(i)
print('cnt = ', cnt)
