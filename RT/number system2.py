#number system
##cnt0 = 0
##cnt1 = 0
##cnt = 0
##for n in range(0, 32):
##    cnt0 = 0
##    cnt1 = 0
##    
##    while n > 0:
##        if n % 2 == 0:
##            cnt0 += 1
##        else:
##            cnt1 += 1
##        n //= 2
##    if cnt0 + 1 == cnt1:
##        cnt += 1
##print(cnt)

cnt = 0
for i in range(1, 1024):
    if bin(i)[2:].count('1') == bin(i)[2:].count('0') * 4 - 1:
        cnt += 1
print(cnt)
        
    
