S = '+-/*2+354/9-^221/+*35*62^32'
L = list( S )
for p in range(len(L)):
    if'0' <= L[p] <= '9':
        L[p] = eval(L[p])

while len(L) > 2:
    for p in range(len(L) - 2):
        if type(L[p]) is int:
            continue
        if type(L[p + 1]) is str:
            continue
        if type(L[p + 2]) is str:
            continue
        a, b = L.pop(p + 1), L.pop(p + 1)
        if L[p] == '+':
            L[p] = a + b
        elif L[p] == '-':
            L[p] = a - b
        elif L[p] == '*':
            L[p] = a * b
        elif L[p] == '/':
            L[p] = a // b
        else:
            L[p] = a ** b
        break
    print(L)
print(L[0])
