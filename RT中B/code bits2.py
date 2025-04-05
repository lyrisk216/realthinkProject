#code bits
def txtcode(txt, key):
    codeList = []
    for i in range(len(txt)):
        codeList.append(key.index(txt[i]))
    return codeList
#----
key = ' .M'
while True:
    n = eval(input('n = '))
    pStr = ''
    for i in range(4):
        pStr = key[n % 4] + pStr
        n //= 4
    print(pStr)
