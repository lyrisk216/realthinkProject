#
num = eval(input('num = '))
fList = [0]
bList = [0]
b = 0
button = 0
flag = 0
for f in range(1, num + 1):
    while True:
        b += 1
        if b == 13 or '4' in str(b):
            continue
        break
    print('Floor:', f, '\tButton:', b)
    fList.append(b)
print(fList)

for i in range(1, num + 1):
    while True:
        if i == 13 or '4' in str(i):
            bList.append(0)
            break
        button += 1
        bList.append(button)
        break
print(bList)
    
    
