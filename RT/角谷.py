#jiaogu

def jiaogu(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 + 1
#----main----
while True:
    n = eval(input('n = '))
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
