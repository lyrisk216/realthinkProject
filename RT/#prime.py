###prime
##n = eval(input('n = '))
##flag = True
##for i in range(2, n):
##    if n % i == 0:
##        flag = False
##        break
##print(flag)
    

n = eval(input('n = '))

for j in range(n, 0, -1):
    flag = True
    for i in range(2, j):
        if j % i == 0:
            flag = False
            break
    if flag == True:
        print('MinPrime = ', j)
        break

    
        
        
