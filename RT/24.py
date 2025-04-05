#RT Lesson 计算4张牌 24点
#V1.1 处理括号
pList = eval(input('4 poker cards: '))

cList = ['+', '-', '*', '/']

kList = []

kList.append( ['', '', '', '', '', '' ])#1 k0

kList.append( ['(', '', ')', '', '', '' ])#2 k0, k2
kList.append( ['', '(', '', '', ')', '' ])#3 k1, k4
kList.append( ['', '', '', '(', '', ')'])#4 k3, k5
kList.append( ['(', '', '', '', ')', ''])#5 k0, k4
kList.append( ['', '(', '', '', '', ')' ])#6 k1, k5
kList.append( ['(', '', ')', '(', '', ')' ])#7 k0, k2, k3, k5
for p1 in range(4):
    for p2 in range(4):
        if p1 == p2:
            continue
        for p3 in range(4):
            if p1 == p3 or p2 == p3:
                continue
            p4= 6 - p1 - p2- p3
            for c1 in range(4):
                for c2 in range(4):
                    for c3 in range(4):
                        for k in kList:
                            
                            s = k[0] +\
                                str(pList[p1]) + cList[c1] + k[1] +\
                                str(pList[p2]) + k[2] + cList[c2] + k[3] + \
                                str(pList[p3]) + k[4] + cList[c3] + \
                                str(pList[p4]) + k[5]
                            try:
                                if 23.9 < eval(s) and eval(s) <= 24.1:
                                    print(s)
                            except:
                                pass
                       
                
            
        
    
