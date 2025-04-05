#Mobile
mList = ['0 ', '1', '2abcABC', '3defDEF',
         '4ghiGHI', '5jklJKL', '6mnoMNO',
         '7pqrsPQRS', '8tuvTUV', '9wxyzWXYZ']
cnt = 0
word = 'good boy'
output = ''
for c in word:
    for i in mList:
        cnt = 0
        for j in i:
            cnt += 1
            if c == j:
                for a in range(cnt):
                    #print(i[0], end = '')
                    output += i[0]
    #print('*', end = '')
    output += '*'
print(output)



myinput = output
output = []
temp = []
cnt = 0

for c in myinput:
    if c == '*':
        print(temp[cnt - 1], end = '')
        cnt = 0
    else:
        temp = mList[ord(c) - 48]
        cnt += 1
    
    
        
        
        
        
    



                

    
