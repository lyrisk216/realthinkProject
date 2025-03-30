#Factorial
n = eval(input('n = '))
f = 1
cnt = 0

for i in range(1, n + 1):
    f *= i
##print('f = ', f)

#字符串法
for i in range(len(str(f)) - 1, 0, -1):
    if str(f)[i] == '0':
        cnt += 1
    else:
        break
print('zero = ', cnt)
#除十法
cnt = 0
while f % 10 == 0:
    f //= 10
    cnt += 1
print('zero = ', cnt)

#数五法
cnt = 0
for i in range(1, n + 1):
   while i % 5 == 0:
       i //= 5
       cnt += 1
print('zero = ', cnt)

#最优法
cnt = 0
while True:
    n = n // 5
    cnt += n
    if n < 5:
        break
print(cnt)

        
    
