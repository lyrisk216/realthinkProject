#pattern
n = eval(input('n = '))
cnt = 0
for y in range(n):
    cnt = 0
    
    for x in range(n - 1 - y):
        print(' ', end = '')
     
    for x in range(y + 1):  #把2y+1个循环拆成y+1个上升和y个下降
        ##print('*', end = '')
        cnt += 1
        print(cnt, end = '')
        
    for x in range(y):
        cnt -= 1
        print(cnt, end = '')
    print()
