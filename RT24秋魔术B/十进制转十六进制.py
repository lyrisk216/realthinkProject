#十转十六进制
while True:
    sstr = ''
    base2 = 3
    n = eval(input('n = '))

    while n > 0:
    ##    if n % 2 == 0:
    ##        sstr = '0' + sstr
    ##    else:
    ##        sstr = '1' + sstr
        if  n % base2 < 10:
            #sstr = str(n % 16) + sstr
            sstr = chr(n % base2 + 48) + sstr
    
        else:
            sstr = chr(n % base2 + 55) + sstr

        n //= base2
    print(sstr)

