n = input()
a = input()
xLst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
nLst = []
if n == 'E':
    w = ''
    cnt = 0
    x = 0
    for i in range(len(a)):
        if x == 0:
            x = a[0]
            continue
        if a[i] == x:
            cnt +=1
        else:
            w += x
            w2 = 'F'+x
            while cnt >=16:
                w +=w2
                cnt-=16
            w+= xLst[cnt]
            cnt = 0
            x = a[i]
    if x != 0:
        w += x
        w2 = 'F'+x
        while cnt >=16:
            w +=w2
            cnt-=16
        w+= xLst[cnt]
    print(w)
elif n == 'EV':
    x = 0
    w = ''
    cnt = 0
    for i in range(len(a)):
        if x == 0:
            x = a[0]
        if a[i] == x:
            cnt +=1
        else:
            w += x
            if cnt <16:
                w+= xLst[cnt]
            else:
                w+='-'
                n2 = hex(cnt)[2:]
                for j in range(len(n2)):
                    if '0' <= n2[j] <= '9':
                        w += n2[j]
                        continue
                    x2 = ord(n2[j])
                    x2 -= 32
                    w += chr(x2)
                w += '-'
            cnt = 1
            x = a[i]
    if x != 0:
        w+= x
        if cnt <16:
            w+= xLst[cnt]
        else:
            w+='-'
            n2 = hex(cnt)[2:]
            for j in range(len(n2)):
                if '0' <= n2[j] <= '9':
                    w += n2[j]
                elif 'a'<=n2[j]<='f':
                    x2 = ord(n2[j])
                    x2 -= 32
                    w += chr(x2)
            w +='-'
    print(w)
elif n == 'D':
    w = ''
    s=0
    for i in range(len(a)):
        if s == 0:
            x = a[i]
            s=1
        else:
            for j in range(xLst.index(a[i])+1):
                w += x
            s=0
    print(w)
elif n == 'DV':
    w = ''
    s = 0
    cnt = 0
    w2 = ''
    r = 1
    for i in range(len(a)):
        if s == 0:
            x = a[i]
            s = 1
        else:
            if a[i] == '-' and s == 1:
                s = 2
                continue
            if s == 2:
                if a[i] == '-':
                    while w2!='':
                        cnt += r*xLst.index(w2[-1])
                        r *= 16
                        w2 = w2[:-1]
                    for j in range(cnt):
                        w += x
                    s,cnt,r = 0,0,1
                else:
                    w2 += a[i]
            else:
                for j in range(xLst.index(a[i])):
                    w += x
                s=0
    if(s == 2):
        while w2!='':
            cnt += r*xLst.index(w2[-1])
            r *= 16
            w2 = w2[:-1]
            for j in range(cnt):
                w += x
    elif (s == 1):
        for j in range(xLst.index(a[i])):
            w += x
    print(w)
