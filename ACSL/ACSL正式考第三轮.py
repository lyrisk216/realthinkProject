#
inputStr = input()
a = inputStr.split(" ")
inc = eval(a[0])
m = eval(a[1])
n = eval(a[2])
rm = 0
rn = 0
while True:
    rm += 1
    mTemp = m
    m = m - (1 + inc * (rm - 1))
    if m <= 0:
        break
    
while True:
    rn += 1
    nTemp = n
    n = n - (1 + inc * (rn - 1))
    if n <= 0:
        break
    
print(abs(rm - rn) + abs(nTemp - mTemp))  
        
