#RT Lesson 剪刀石头布游戏
#V1.0
import random

p = 0
c = 0
nameList = ['stone', 'scissors', 'paper']
cnt = 0
while True:
    pNum = eval(input('1:stone, 2:scissors, 3:paper, other:quit'))
    sNum = random.randint(1, 3)
    if not (pNum in [1, 2, 3]):
        break
    cnt += 1
    print('Computer -', nameList[ cNum - 1 ], ' : ', \
            nameList[ pNum - 1 ], '- Player')
    if (pNum - cNum) % 3 == 2:
       print('You win')
    elif (pNum - cNum) % 3 == 1:
        print('You lose')
    else:
        print('Tie')
print('Final:')
print('total:', cnt )
#请输出胜负统计：总局数， 胜负平的百分比
