#sqrt
n = 2
m = eval(input('m = '))
p = eval(input('p = '))
t = 10 ** p
bottom, top = 0, m 
while True:
    a = (bottom + top) / 2
    print(a, bottom, top)
    if int(bottom * t) == int(top * t):
        print(int(top * t) / t)
        break
    if 2 ** a > m:
        top = a
    elif 2 ** a < m:
        bottom = a
    
