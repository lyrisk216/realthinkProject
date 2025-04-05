#zzxc
##n1, n2 = eval(input('n1, n2='))
##while True:
##    n = n1 % n2
##    print(n1, n2, n)
##    if n == 0:
##        break
##    n1, n2 = n2, n
##print('GCF=', n2)

n1, n2 = eval(input('n1, n2 = '))
while n1 % n2 > 0:
    n = n1 % n2
    print(n, n1, n2)
    n1, n2 = n2, n
print('GCF=', n2)
    
