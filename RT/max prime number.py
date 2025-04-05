#max prime
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False22
    return True
#-----main------
n = eval(input('n = '))
##for a in range(n, 0, -1):
##    if n % a == 0:
##        if is_prime(a):
##            print(a)


for i in range(n, 0, -1):
    if is_prime(i):
        print(i)
        break
    


            


        




         
