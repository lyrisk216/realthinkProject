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
    if d > get_days_num(y, m):
        d += 1
    if mList[(m - 1)] < d:
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
y0, m0, d0, w0 = eval (input('Base line : year, month, day, weekNum : '))
y, m, d = y0, m0, d0
y1, m1, d1 = eval(input('Target : year, month, day:'))
while True:
    if y1 > y0:
        print('未来')
        break
    elif y0 > y1:
        print('过去')
        break
    else:
        if m1 > m0:
            print('未来')
            break
        elif m0 > m1:
            print('过去')
            break
        else:
            if d1 > d0:
                print('未来')
                break
            elif d0 > d1:
                print('过去')
                break
            else:
                print('1111')
                break
##for i in range(150):
    
##    print(i, 'days later:', y, m, d, wList[(i + w0) % 7 ])
##    y, m, d = next_day(y, m, d)
##    print(i, 'days before:', y, m, d, wList[(i + w0) % 7 ])
##    y, m, d = last_day(y, m, d)

