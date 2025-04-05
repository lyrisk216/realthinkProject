#hex2dec

    n = eval(input('n = '))
    w = ''
    while n > 0:
        h = n % 16
        print(h)
        if h < 10:
            w = str(h) + w
        else:
            w = chr(ord('A') + h - 10) + w
        n //= 16
    print(w)
