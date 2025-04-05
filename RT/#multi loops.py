#multi loops
'''
for y in range(10):
    for x in range(10):
        print('y = ', y, 'x = ', x, end = '\t')
    print()
'''
cnt = 0 
for a in range(1, 10):
    for b in range(0, 9, 2):
        if a == b:
            continue
        for c in range(1, 10, 2):
            if a == c:
                continue
            for d in range(0, 10):
                if a == d or b == d or c == d:
                    continue
                print(a, b, c, d)
                cnt += 1
print('cnt = ', cnt)
