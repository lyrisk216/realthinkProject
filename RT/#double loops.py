#double loops
##
##for y in range(10):
##    for x in range(10):
##        print('y = ', y, 'x = ', x, end = '\t,')
##    print()

##n = eval(input('n = '))
##for y in range(n):
##    for x in range(n  - 1 - y):
##        print(' ', end = ' ')
##    for y in range(y + 1 + y):
##        print('*', end = ' ')
##    print()
##    
##
##for y in range(n - 2, -1, -1):
##    for x in range(n  - 1 - y):
##        print(' ', end = ' ')
##    for y in range(y + 1 + y):
##        print('*', end = ' ')
##    print()
a = 1
n = eval(input('n = '))
for y in range(n):
    for x in range(n - 1 - y):
        print(' ', end = '')
    print(a * a)
    a = a * 10 + 1


#circle
##r = eval(input('r = '))
##for y in range(-r, r + 1):
##    for x in range(-r, r + 1):
##        if x * x + y * y <= r * r:
##            print('*', end = ' ')
##        else:
##            print(' ', end = ' ')
##    print()

