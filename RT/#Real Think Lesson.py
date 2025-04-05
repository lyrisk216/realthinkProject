#Real Think Lesson

import random

s, n = eval(input('金额, 人数: '))
mList = [1] * n
cents = int(s * 100 - n)

for i in range(n - 1):
    r = random.randint(0, int(cents / (n - i) + 0.5))
    mList[1] += r
    cents -= r
mList[n - 1] += cents

for i in range(n):
    print(mList[i] / 100)
