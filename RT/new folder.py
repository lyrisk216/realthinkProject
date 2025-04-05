#
def count_word( txt, word ):
    cnt = 0
    for p in range( len( txt ) ):
        if txt[ p: p + len( word ) ] == word:
            cnt += 1
    return cnt
#--- main ---
f = open( 'news.txt', 'r' )
lineList = f.readlines( )
f.close( )
nList = []
aList = []

wList = ['曼联', '曼城', '阿森纳', '利物浦', '切尔西', '热刺']
aList = ['曼联', '曼城', '阿森纳', '利物浦', '切尔西', '热刺']
dList = [0] * len(wList)
for w in range(len(wList)):
    for line in lineList:
        dList[w] += count_word( line, wList[w] )
        
    print( wList[w], '\t:', dList[w] )
    nList.append(dList[w])
for a in range(len(nList)- 1):
    flag = 0
    for i in range(len(nList) - 1 - a):
        #从大到小排序，判断顺序是否正确
        if nList[i] < nList[i + 1]:
            nList[i], nList[i + 1] = nList[i + 1], nList[i]
            aList[i], aList[i + 1] = aList[i + 1], aList[i]
            flag = 1
    #print(nList)
    if flag == 0:
        break
print()
print(aList)       
