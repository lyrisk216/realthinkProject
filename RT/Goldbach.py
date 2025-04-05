#Goldbach
n = eval(input('n = '))
for n1 in range(2, n - 1):
    flag = True
    for i in range(2, n1):
        if n1 % i == 0:
            flag = False
            break
    if flag == False:
        continue
    n2 = n - n1
    for i in range(2, n2):
        if n2 % i == 0:
            flag = False
            break
    if flag == True:
        if n1 >= n2:
            break
        else:
            print(n1, n2)
    
