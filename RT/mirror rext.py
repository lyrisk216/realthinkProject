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
def is_mirror2(w):
    w1 = ''
    w2 = ''
    for c in w:
        w1 = cap(c) + w1
        w2 = w2 + cap(c)
    return w1 == w2
#-- main --
while True:
    word = input('word = ')
    print(is_mirror(word))
    print(is_mirror2(word))
