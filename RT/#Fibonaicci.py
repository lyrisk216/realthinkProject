#Fibonaicci
num = eval(input('num = '))
n1 , n2 = 0, 1
n = n1 + n2
print(n1, n2, n)
while True:
    n1, n2 = n2, n
    n = n1 + n2
    if n > num:
        break
    print(n)
    
