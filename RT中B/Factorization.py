#
n = eval(input('n = '))
fStr = str(n) + ' = '
for i in range(2, n + 1):
    while n % i == 0:
        n //= i
        fStr += str(i) + '*'
print(fStr[:-2])
      
    
        
    
        
