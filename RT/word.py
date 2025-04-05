#word
txt = 'This is a book!!!'
wList = []
word = ''

for c in txt:
    if 'A' <= c <= 'z' or 'a' <= c <= 'z':
        word += c
    elif word != '':
        wList.append(word)
        word = ''
    #print(c, word, wList)
if len(word) > 0:
    wList.append(word)
print(wList)
