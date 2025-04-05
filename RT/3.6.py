#sqrt
x = eval(input('x(x > 1), point = '))
t = 10 ** point
bottom, top = 1, x
while bottom != top:
    a = (bottom + top) / 2
    print(a, bottom, top)
    if int(bottom * t) == int(top * t):
        print(int(top * t) / t)
        break
    if a * a > x:#move top down
        top = a
    elif a * a < x: #mpve bottom up
        bottom = a
    else:
        print('Got it')
        break
  


