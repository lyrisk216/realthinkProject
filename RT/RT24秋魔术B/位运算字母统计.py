#位运算字母统计
def cap(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32)
    else:
        return c
#---main---
aBits = 0
while True:
    word = input('word = ')
    if word == '':
        print('finished')
        break
    for c in word:
        if 'A' <= cap(c) <= 'Z':

            aBits = aBits | ( 1 << (ord(cap(c)) - ord('A')) )
        print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        bStr = (bin(aBits)[2:])[::-1]
        print((bStr + '0' * 25)[:26])
while True:
    c = cap(input('chr = '))
    flag = 'No'
    if'A' <= c <= 'Z':
        if aBits & ( 1 << (ord(c) - ord('A')) ) > 0:
            flag = 'Yes'
    print(flag)
    
