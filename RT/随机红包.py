#ReakThink Lesson


import random

##s, n = eval(input('amount, num : '))

s = 200
n = 10
countList = [0] * n
countList2 = [0] * n

for j in range(100000):
    mList = [1] * n
    cents = int(s * 100 - n)

    for i in range(n - 1):

        
        r = random.randint(0, int(cents / (n - i) * 2))

        mList[i] += r
        cents -= r
        
    mList[n - 1] += cents

    for i in range(n):
        if mList[i] >= (s * 100) / 2:
            countList[i] += 1
        if mList[i] == 1:
            countList2[i] += 1

for j in range(n):
    print('第', j+1, '位',':', '拿到超大红包', countList[j], '次')
print()
for j in range(n):
    print('第', j+1, '位',':', '拿到超小红包', countList2[j], '次')
            
##for i in range(n):
##    print(mList[i] / 100)
