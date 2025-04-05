#RT Lesson 24 points
#不处理括号
pList = eval(input('4 poker card: '))
cList = ['+', '-', '*', '/']
for p1 in range(4):
    for p2 in range(4):
            if p1 == p2:
                continue
            for p3 in range(4):
                if p1 == p3 or p2 == p3:
                    continue
                p4 = 6 - p1 - p2 - p3
                for c1 in range(4):
                    for c2 in range(4):
                        for c3 in range(4):
                            s = str(pList[p1]) + cList[c1] + \
                                str(pList[p2]) + cList[c2] + \
                                str(pList[p3]) + cList[c3] + \
                                str(pList[p4])
                            if eval(s) == 24:
                                print(s)
