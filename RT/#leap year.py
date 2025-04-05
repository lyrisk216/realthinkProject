#leap year
def is_leap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False
def is_leap2(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def is_leap(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return True
    else:
        return False

#-----main-----
mList = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    y, m = eval(input('year, month = '))
    if m == 2:
        print(28 + is_leap(y))
        else:
            print(mList[m - 1])

    
