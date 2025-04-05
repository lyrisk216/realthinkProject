#next day
def is_leap(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
def get_days_num(y, m):
    mList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mList[1] += is_leap(y)
    return mList[m - 1]
def next_day(y, m, d):
    mList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d += 1
    if d > get_days_num(y, m):
        d = 1
        m += 1
        if m > 12:
            y += 1
            m = 1
    
    return y, m, d

def last_day(y, m, d):
    
    mList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            y -= 1
            m = 12
        d = get_days_num(y, m)
    return y, m, d
    
    

#--- main ---
wList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y0, m0, d0, w0 = eval (input('Base date : year, month, day, weekNum : '))
y, m, d = y0, m0, d0
y1, m1, d1 = eval (input('Object date : year, month, day : '))
isFuture = True
if y0 == y1:
    if m0 == m1:
        if d0 <= d1:
            isFuture = True
        elif d0 > d1:
            isFuture = False
    elif m0 < m1:
        isFuture = True
    elif m0 > m1:
        isFuture = False
elif y0 < y1:
    isFuture = True
else:
    isFuture = False


if isFuture == True:
    i = 0
    while True:
        if y == y1 and m == m1 and d == d1:
            print(i, 'days later:', y, m, d, wList[(i + w0) % 7 ])
            break
        i += 1
        y, m, d = next_day(y, m, d)
else:
    i = 0
    while True:
        i += 1
        y, m, d = last_day(y, m, d)
        if y == y1 and m == m1 and d == d1:
            print(i, 'days before:', y, m, d, wList[(-i + w0) % 7 ])
            break
