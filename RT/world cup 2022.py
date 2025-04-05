#world cup 2022
import random

teamList = []
teamList.append(['卡塔尔', '巴西', '比利时', '法国',
                 '阿根廷', '英格兰', '西班牙', '葡萄牙' ])
teamList.append(['墨西哥', '丹麦', '瑞士', '美国',
                 '克罗地亚', '荷兰', '德国', '乌拉圭'])
teamList.append(['伊朗 ', '韩国', '塞内加尔', '摩洛哥',
                 '波兰', '塞尔维亚', '突尼斯', '日本'])
teamList.append(['加纳', '厄瓜多尔', '喀麦隆', '哥斯达黎加',
                 '威尔士', '澳大利亚', '沙特', '加拿大'])
                 f
groupList = []
for i in range(8):
    group = []
    group.append(teamList[0][i])
    groupList.append(group)
print(groupList)
for g in range(1, 4):
    print('Level', g)
    for i in range(8):
        input('Chou!')
        r = random.randint(0, len(teamList[g]) - 1)
        groupList[i].append(teamList[g][r] )
        teamList[g].pop(r)
        print(groupList[i])
    print()
print(groupList)
f = open( 'group result.txt', 'w' )
txt = ''
for g in range(8):
    for i in range(4):
        txt += groupList[g][i] + ' '
    txt += '\n'
f.write(txt)
f.close()
