#十六进制转十进制
while True:
    temp = 0
    decNum = 0
    n = input('n = ')
    for i in range(len(n)):
        if ord(n[i]) <= 57 and ord(n[i]) >= 48:
            temp = ord(n[i]) - 48
        elif ord(n[i]) <= 70 and ord(n[i]) >= 65:
            temp = ord(n[i]) - 55
        else:
            print('......')
            break

        decNum = decNum * 16 + temp
    print(decNum)
        
    



