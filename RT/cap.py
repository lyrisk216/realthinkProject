#cap
def cap(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32)
    else:
        return c
#---main---
word = 'Hello world!'
nw = ''
for c in word:
    nw += cap(c)
print(nw)
    
    
