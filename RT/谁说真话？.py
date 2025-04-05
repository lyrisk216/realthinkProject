#goodman
for gm in range(4):#0:A 1:B 2:C 3:D
    cnt = 0
    if gm != 0:
        cnt += 1
    if gm == 2:
        cnt += 1
    if gm == 3:
        cnt += 1
    if gm == 2:
        cnt += 1
    if cnt == 3:
        print(chr(gm + ord('A')))
    if (gm != 0) + (gm == 2) + (gm == 3) + (gm == 2) == 3:
        print(chr(gm + ord('A')))
        

    
    
