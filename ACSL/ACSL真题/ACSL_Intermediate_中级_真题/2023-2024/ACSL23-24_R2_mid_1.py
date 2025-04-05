# 测试数据
txt = '''ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.  With countrywide and worldwide participants, it became the American Computer Science League.  It has been in continuous existence since 1978.  Each yearly competition consists of 4 regular-season contests.  All students at each school may compete but the team score is the sum of the best 3 or 5 top scores.  Each contest consists of two parts: a written section (called shorts) and a programming section.  Written topics tested include what does this program do, digital electronics, Boolean algebra, computer numbering systems, recursive functions, data structures (primarily dealing with heaps, binary search trees, stacks, and queues), Lisp programming, regular expressions and Finite State Automata, bit string flicking, graph theory, assembly language programming, and prefix/infix/postfix notation.  '''
location = '3.5.1 8.21.9 1.10.8 2.7.2 7.15.6 5.4.3 4.10.3 6.18.1'


# txt = input()
# location = input()

#---------建立数据list--------------
lList = location.split(' ')

for i in range(len(lList)):
    lList[i] = lList[i].split('.') # 生成字母位置 双层list
for i in range(len(lList)):
    for ii in range(len(lList[i])):
        lList[i][ii] = int(lList[i][ii]) # 将每个str转化为int
aList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
         'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
         'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
tList = txt.split('  ') # 第一步处理数据，整理出句子
for i in range(len(tList)):
    tList[i] = tList[i].split(' ') # 第二步处理数据，整理出词汇

#------------第一次处理符号(如果符号在词的最前、最后)，删除第一层符号---------------
for x in range(len(tList)):
    for y in range(len(tList[x])):
        try: # 在删除符号后可能会出问题，因此用try
            for n in range(len(tList[x][y])): # 在每个词语中处理掉符号
                flag = 0
                for i in range(len(aList)):  # 看每个字母是不是符号 (flag = 0: 符号, flag = 1: 字母)
                    if tList[x][y][n] == aList[i]: #如果字母和字母list中重合
                        flag = 1
                    else:
                        continue
                if flag == 1:
                    continue
                else:  # 如果字母是符号（没有在字母list中出现）：
                    if n == 0:  # 如果符号是在词语最前面
                        tList[x][y] = tList[x][y][1:] #删除符号
                    elif n == len(tList[x][y]) - 1: #如果符号在词语后面
                        tList[x][y] = tList[x][y][:-1] #删除符号
        except IndexError:
            continue
#------------第二次处理符号（处理符号在词的中间，以及词语开头、结尾有两个连续符号的情况！！）
for x in range(len(tList)):
    for y in range(len(tList[x])):
        for n in range(len(tList[x][y])):
            flag = 0
            for i in range(len(aList)):  # 和上面一样
                try:
                    if tList[x][y][n] == aList[i]:
                        flag = 1
                    else:
                        continue
                except IndexError:
                    continue
            if flag == 1:
                continue
            else:
                if n == 0:
                    tList[x][y] = tList[x][y][1:]
                elif n == len(tList[x][y]) - 1:
                    tList[x][y] = tList[x][y][:-1]
                else:  # 如果符号在词语中间
                    for g in range(len(tList[x][y])):  # 找到符号在词语中的位置
                        rflag = 0 # 这个字母是不是符号 (flag = 0: 符号, flag = 1: 字母)
                        for f in range(len(aList)):
                            try: #避免把符号从list删除后list不够长导致的error
                                if tList[x][y][g] == aList[f]: #把字母和字母list中一一核对，如果没有核对成功则是符号
                                    rflag = 1
                            except IndexError:
                                continue
                        if rflag == 0: #如果这个字母是符号
                            try: #避免list不够长的错误
                                arList = tList[x][y].split(tList[x][y][g]) #把当前word在前面按照查出的符号split开来
                            except IndexError:
                                continue
                            tList[x].pop(y) #删除原来有符号的词
                            for i in range(len(arList)):
                                tList[x].insert(y + i, arList[i]) #按照顺序把整理出来的词语一一插入list

fin = ''
for i in range(len(lList)):
    sentence = lList[i][0] - 1
    word = lList[i][1] - 1
    letter = lList[i][2] - 1
    try:
        fin = fin + tList[sentence][word][letter] #找出题中要求的字母
    except IndexError:
        fin = fin + ' ' #如果字母不存在则用空格替代
print(fin)


