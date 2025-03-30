#code bits
def txtcode(txt, key):
    codeList = []
    for i in range(len(txt)):
        codeList.append(key.index(txt[i]))
    return codeList
#-----
m = []
m.append('MMMMMM  ')
m.append(' MM..MM.')
m.append(' MM. MM.')
m.append(' MMMMM. ')
m.append(' MM..MM.')
m.append(' MM. MM.')
m.append('MMMMMM. ')
m.append(' ...... ')
key = ' .M'
binCodeList = ['00', '01', '10', '11']
for line in m:
    print(line)
    cList = txtcode(line, key)
    print(cList)
    binStr = ''
    for v in cList:
        binStr += binCodeList[v]
    print(binStr, int(binStr, 2) // 256, int(binStr, 2) % 256)
while True:
    n = eval(input('n = '))
    pStr = ''
    for i in range(4):
        pStr = key[n % 4] + pStr
        n //= 4
    print(pStr)

