#RT Lesson 高精度计算 V0.9

PRECISION = 100

def insert_string(string, index, insert_str):
    return string[:index] + insert_str + string[index:]  #字符串插入(百度搜索)

def RT_num_init(nStr):
    n = 0
    nPointPos = 0
    nList = [0] * PRECISION
    for i in range(len(nStr)):
        if nStr[len(nStr) - i - 1] == '.':
            nPointPos = i                       #记录小数点位置
        else:
            nList[n] = ord(nStr[len(nStr) - i - 1]) - 48            #将整数部分加入list
            n += 1
    return nList, nPointPos                         

def RT_print_num(nList, nPointPos):
    flag = 0
    nStr = ''
    for i in range(len(nList)):
        n = nList[len(nList) - i - 1]
        if n > 0:                   
            flag = 1
        if flag == 1:
            nStr = nStr + str(n)
    if flag == 0:
        nStr = str(0)
    if nPointPos > 0:
        nStr = insert_string(nStr, len(nStr) - nPointPos, '.')
    print(nStr)
    return

def RT_add(nx1List, n1PointPos, nx2List, n2PointPos):
    n1List = nx1List[:]         #复制list
    n2List = nx2List[:]
    nList = [0] * PRECISION
    carry = 0
    nPointPos = 0
    n = 0
    if n1PointPos == n2PointPos:    
        nPointPos = n1PointPos
    elif n1PointPos > n2PointPos:
        nPointPos = n1PointPos
        n = n1PointPos - n2PointPos
        for i in range(n):
            n2List.insert(0, 0)         #乘10
            n2List.pop()                #保持长度
    else:
        nPointPos = n2PointPos          
        n = n2PointPos - n1PointPos
        for i in range(n):
            n1List.insert(0, 0)
            n1List.pop()
            
    for i in range(PRECISION):
        s = n1List[i] + n2List[i] + carry
        nList[i] = s % 10
        carry =  s  // 10
    return nList, nPointPos

def RT_times(n1List, n1PointPos, n2List, n2PointPos):
    nList = [0] * PRECISION
    for i in range(PRECISION):
        nmList = [0] * PRECISION
        for j in range(n2List[i]):
            #print(j)
            nmList, temp = RT_add(nmList, 0, n1List, 0)         #只加整数部分, 小数点最后处理
            #print(n1List)
        for j in range(i):
            nmList.insert(0, 0)
            nmList.pop()
        nList, temp = RT_add(nList, 0, nmList, 0)
    return nList, n1PointPos + n2PointPos

#---main---
n1PointPos = 0
n2PointPos = 0
n1List, n1PointPos = RT_num_init(input('n1 = '))
n2List, n2PointPos = RT_num_init(input('n2 = '))
nList, pos1 = RT_add(n1List, n1PointPos, n2List, n2PointPos)
print('n1 + n2 = ', nList,pos1)
RT_print_num(nList, pos1)
nList, pos1 = RT_times(n1List, n1PointPos, n2List, n2PointPos)
print('n1 * n2 = ', nList, pos1)
RT_print_num(nList, pos1)

