#prime number
n = eval(input('n = '))

flag = True
for a in range(1000):
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
print(flag)
    
