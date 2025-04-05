#mirror text
def cap(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32)
    else:
        return c
def is_mirror(w):
    for i in range(len(w) // 2):
        if cap(w[i]) != cap(w[len(w) - 1 - i]):
            return False
    return True
#-- main --
n = eval(input('n = '))
cnt = 0
for i in range(int((10 ** n) ** 0.5) + 1):
    if is_mirror(str(i * i)):
        print(i * i)
        cnt += 1
print('cnt = ', cnt)
