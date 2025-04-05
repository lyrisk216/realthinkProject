#键盘打字
pList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'caps lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
flag = -1
cnt = 0
for i in range(200):
    if pList[i % 27] == 'caps lock':
        flag = -flag
        cnt += 1
    print(flag, pList[i  % 27])
print('屏幕上有', 200 - cnt, '个字母显示')

