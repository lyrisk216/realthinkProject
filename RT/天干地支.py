#天干地支
#公元4年是甲子年
hsList = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
ebList = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
zList = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
while True:
    y = eval(input('year = '))
    if y == 0:
        print('......')
    if y < 0:
        y += 1
    hsId = (y - 4) % 10
    ebId = (y - 4) % 12
    print(hsList[hsId], ebList[ebId], zList[ebId])
