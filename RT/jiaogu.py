#jiaogu

def callboss(x):
    if x % 2 == 0:
        x = x // 2
    else:
        x = x * 3 + 1
        print( x )
        if x == 1:
            return 1
        else:
            return callboss( x )
#----main----
n = eval(input('n = '))
print('call boss : ', callboss( n ))
