#Goldbach Function
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
#-------main--------
n = eval(input('n = '))
for n1 in range(2, n // 2 + 1):
    if is_prime(n1) == True and is_prime(n - n1) == True:
        print(n1, n - n1)
            
