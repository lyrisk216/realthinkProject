#number system
while True:
    n, base = eval(input('n, base = '))
    w = ''
    while n > 0:
        a = n % base
        print(a)
        if a < 10:
            w = str(a) + w
        else:
            w = chr(ord('A') - 10 + a) + w
        n //= base
    print(w)
