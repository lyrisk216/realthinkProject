#Fibonacci
a, b = eval(input('a, b = '))
n1, n2 = 0, 1
n = n1 + n2
s = 0
cnt = 0
aList, bList, fList = [], [], []
while n <= b:
    if n >= a:
        if cnt % 2 == 0:
            aList.append(n)
        else:
            bList.append(n)
        fList.append(n)
        cnt += 1
        s+= n
    n1, n2 = n2, n
    n = n1 + n2
print('cnt = ', cnt)
print('sum = ', s)
print(fList)
print(aList)
print(bList)
    
    
