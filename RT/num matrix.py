#num matrix
n = eval(input('n = '))
'''
for y in range(n):
    for x in range(n):
        print(y * n + x, end = '\t')
    print()
'''
for y1 in range(2 * n - 1):
    y = n - 1 - abs(n - 1 - y1)
    print(' ' * (n - 1 - y), end = '')
    for x in range(2 * y + 1):
        print(y + 1 - abs(y - x), end = '')
    print()
