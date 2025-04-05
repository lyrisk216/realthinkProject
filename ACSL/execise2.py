def reverse_string(s):
    return s[::-1]

def isH(s):
    if s == reverse_string(s):
        return True
    return False
    


# --- main ----
cnt = 0
for i in range(1, 9999999+1):
    decNum = str(i)
    #binNum = bin(i)[2:]
    octNum = oct(i)[2:]
    #print(decNum, binNum, octNum)
    if isH(decNum) and isH(octNum):
        cnt += 1
        print(cnt, i, oct(i)[2:])
    
        
    
    
