#Goldbach
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#-----main-----
n = eval(input('n = '))
for n1 in range(2, int(n / 2) + 1):
    if is_prime(n1) and is_prime(n - n1):
        print(n1, n - n1)
