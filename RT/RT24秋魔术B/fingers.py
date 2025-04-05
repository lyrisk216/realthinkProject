#fingers
##fList = ['big', 'eat', 'mid', 'noname', 'small']
##f = -1
##flag = 1
##for i in range(100):
##    f += flag
##    if f == 5 or f == -1:
##        flag *= -1
##        f += 2 * flag
####    if f == 5:
####        flag = -1
####        f = 3
####    if f == -1:
####        flag = 1
####        f = 1
####    print(fList[f])
fList = ['big', 'eat', 'mid', 'noname',
         'small', 'noname', 'mid', 'eat']
num = 100
print(fList[(num - 1) % 8])
