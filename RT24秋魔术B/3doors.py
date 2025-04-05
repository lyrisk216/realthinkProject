#3doors
import random

num = 10000
cntBuhuan, cntHuan = 0, 0
for i in range(num):
    car = random.randint(0, 2)
    dList = [0] * 3
    dList[car] = 1
    guess = random.randint(0, 2)
    if guess == car:
        cntBuhuan += 1
    else:
        rest = 3 - car - guess
        cntHuan += 1
print('Bu huan car:', cntBuhuan)
print('Huan car:', cntHuan)
