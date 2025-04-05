#Fibonaicci
'''
a,b = eval(input('a, b = '))
n1, n2 = 0, 1
cnt = 0
total = 0
print(n1, n2)
while True:
    n = n1 + n2
    if n > b:
        break
    if n >= a:
        cnt += 1
        total += n
    print(n)
    n1, n2 = n2, n
print(cnt, total)  
'''   
a, b = eval(input('a, b = '))
n1, n2 = 0, 1
cnt = 0
s = 0
while n1 + n2 <= b:
    n = n1 + n2
    if n >= a:
        print(n)
        cnt += 1
        s += n
    n1, n2 = n2, n
print('sum = ', s)
print('cnt = ', cnt)
