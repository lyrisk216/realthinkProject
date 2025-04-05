#Fibonacci
num = eval(input('num = '))
n1, n2 = 0, 1
while n <= num:
    n = n1 + n2
    print(n)
    n1 = n1 + (n2 - n1)
    n2 = n2 + (n - n2)
    if n >= 20:
        print(n)
        break
