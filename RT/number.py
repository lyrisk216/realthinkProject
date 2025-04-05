#number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 #----main-----   
while True:
    x = eval(input('x = '))
    if x % 1 == 0:
        print('int')
        if x % 2 == 0:
            print('even')
        else:
            print('odd')
        if x ** 0.5 % 1 == 0:
            print('sqr number')
        if is_prime(x):
            print('prime number')
            
    else:
        print('float')
