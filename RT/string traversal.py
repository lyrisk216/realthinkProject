#string traversal
w = 'Hello world!'
w1 = ''
w2 = ''
for c in w:
    c1 = chr(ord(c) + 2)
    w1 = w1 + c1
    w2 = c1 + w2
    print(c, c1)
print(w1)
print(w2)

w1 = ''
w2 = ''
for i in range(len(w)):
    c = w[i]
    c1 = chr(ord(c) + 2)
    w1 = w1 + c1
    w2 = c1 + w2
    print(i, c, c1)
print(w1)
print(w2)



    
