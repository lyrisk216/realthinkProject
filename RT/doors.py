#doors
num = 100
dList = [0] * (num + 1)
dBits = 0
for w in range(1, num + 1):
    
    for d in range(w, num + 1, w):
        dBits = dBits ^ (1 << d )
for d in range(num + 1):
    if dBits & (1 << d) > 0:

        print(d)
