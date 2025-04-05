#casino
import random

scoreMax = 0
for i in range(3):
    print('Round', i + 1)
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    score = d1 + d2
    if score > scoreMax:
        scoreMax = score
    print('Dicel:', d1, '\tDice2:', d2, '\tScore:', score)
print('Best:', scoreMax)
