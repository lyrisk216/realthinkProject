#base1 => base2
def num2dec(xStr, base):
    n = 0
    for c in xStr:
        if '0' <= c <= '9':
            i = ord(c) - 48
        else:
            i = ord(c) - 55
        n = n * base + i
    return n

def dec2num(decNum, base):
    sstr = ''
    while decNum > 0:
        if  decNum % base < 10:            
            sstr = chr(decNum % base + 48) + sstr    
        else:
            sstr = chr(decNum % base + 55) + sstr
        decNum //= base
    return sstr
#------------
xStr = input('num = ')
base1, base2 = eval(input('base1, base2 = '))
a = num2dec(xStr, base1)
b = dec2num(a, base2)
print(b)


        


    
