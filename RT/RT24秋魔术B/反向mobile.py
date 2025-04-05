#mobile
mList = ['0 ', '1', '2abcABC', '3defDEF',
         '4ghiGHI', '5jklJKL', '6mnoMNO',
         '7pqrsPQRS', '8tuvTUV', '9wxyzWXYZ']
myinput = '44*6666*6666*33*00*222*6666*9999*'
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
    
    
