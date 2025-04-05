#自由进制转换
while True:
    base1 = 2
    hStr = input('hex num = ')
    n = 0
    for c in hStr:
        if '0' <= c <= '9':
            i = ord(c) - 48
        else:
            i = ord(c) - 55
        n = n * base1 + i
    print(n)

  
