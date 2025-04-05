def cap(c):
    if 'a'<= c <= 'z':
        return chr(ord(c) - 32)
    else:
        return c
def count_chr(txt, c0):
    cnt = 0
    for c in txt:
        if cap(c) == cap(c0):
            cnt += 1
    return cnt
#--- main ---
txt = '''The quick brown fox, named Roxanne, jumped over Bruno, a lazydog.'''
cnt = 0
for i in range(26):
    if count_chr(txt, chr(i + ord('a'))) > 0:
        cnt += 1
print('cnt = ', cnt)
lettersFlag = [0] * 26
for c in txt:
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        i = ord(cap(c)) - ord('A')
        lettersFlag[i] = 1
print(lettersFlag)
cnt = 0
for i in range(len(lettersFlag)):
    cnt += lettersFlag[i]
print('cnt = ', cnt)
