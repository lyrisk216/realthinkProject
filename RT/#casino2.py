#casino2
import random

pWin, pLose, tie = 0, 0, 0
points1, points2 = 0, 0
i = 0
while True:
    i += 1
    print('Round', i)
    input('Go!')
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    score1 = d1 + d2
    points1 += score1
    print('Player\tDice1:', d1, '\tDice2:', d2, '\tScore:', score1)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    score2 = d3 + d4
    points2 += score2
    print('cpu\tDice3:', d3, '\tDice4:', d4, '\tScore:', score2)
    if score1 > score2:
        print('you win!')
        pWin +=1
    elif score1 < score2:
        print('you lose!')
        pLose += 1   
    else:
        print('Tie!')
        tie += 1
    print()
    if pWin == 3 or pLose == 3:
        break
print('FINAL')
print('Player\tWin:', pWin, '\tLose:', pLose, '\ttie', tie)
print('Player points:', points1, '\tcpu points:', points2)
if pWin > pLose:
    print('#YOU WIN!')
elif pWin < pLose:
    print('#YOU LOSE')
else:
    if points1 > points2:
        print('You win by points!')
    elif points1 < points2:
        print('You lose by points!')
    else:
        print('TIE')

    
