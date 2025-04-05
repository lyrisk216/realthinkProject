#Montecarlo pi
import random

ns = eval(input('times = '))
nc = 0
for i in range(ns):
    x = random.random() #0~1
    y = random.random()
    if x * x + y * y < 1:
        nc += 1
print('pi = ', nc / ns * 4)
