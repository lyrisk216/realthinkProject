for i in range(1, 32):
    cnt1 = 0
    cnt0 = 0
    a = bin(i)
    a = a[2:]
    for c in a:
        if c == '1':
            cnt1 += 1
        if c == '0':
            cnt0 += 1
    if cnt1 == cnt0:
        print(i, bin(i))
    
