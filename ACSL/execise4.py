#二进制位运算

x = eval(input('x = '))
s = bin(x)[2:]
L = len(s)
if L % 2:
    s = '0' + s
    L += 1
S = list(s)
for p in range(L // 2):
    S[2 * p], S[2 * p + 1] = S[2 * p + 1], S[2 * p]
s = ''
for c in S:
    s = s + c
print(int(s, 2))
