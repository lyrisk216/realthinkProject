#ABCD
for a in range(1, 5):
    for b in range(1, 5):
        if a == b:
            continue
        for c in range(1, 5):
            if a == c or b == c:
                continue
            d = 10 - a - b - c
            if (a == 1 and b != 3) or (b == 3 and a != 1):
                if (c == 1 and d!= 4) or (d == 4 and c!= 1):
                    if (d == 1 and b!= 3) and (b == 3 and d!= 1):
                        print(a, b, c, d)
            if (a ==1) + (b == 3) == 1:
                if (c == 1) != (d == 4):
                    if (d == 1) ^ (b == 3):
                        print(a, b, c, d)
    
        
        
    
        
