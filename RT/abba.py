#abba
while True:
    n, base = eval(input('n, base = '))#abcf -> fcba
    b = n % base
    a = n // base
    print(b * base + a)
