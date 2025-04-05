#ACSL Rack-O
#input:
'''
12 130
20 110 30 16 84 40 91 69 75 7 81 15
33 47 114 55 35 71 25 123 51 23 34 10 100 77 36 115
'''
#HV:小于前一个数字的数字的数量(使数组不是升序排列的数的数量)
#A方法:(drawn card:x, rack:L)
#1.找到interval:(n//s)+1
#2.生成interval列表[(a, b), (c, d), (e, f)]
#3.用x获得在interval列表中的下标p,用此p去牌组里寻址数字y
#4.如果y在合适的interval, 则A为True, 反之为False
#5.A为True:把下标p的数字替换成x
#B方法(循环):
#1.从L第一个非升序元素开始向前切三个数, 获得子数组l
#2.如果x替换l的一个元素使得l是升序排列:B为True,记录被替换的元素的下标p
#3.B为True:替换下标p的数字为x,跳出循环
#4.如果没有符合条件的l:从下一个非升序元素开始向前切3个数,重复步骤1
#5.如果遍历结束没有符合条件的l:B为False
#分别计算A和B情况下的L列表的HV,采用HV最小的那个方法(默认A)
#如果A和B都为False:跳过, 下一个x
#结束条件:当xL为空或者HV为零
#---------- def ---------
def interval(s, n):
    if n % s  == 0:
        interval = n // s
    else:
        interval = n // s + 1
    inL = []
    #print(interval)
    i = 1
    while interval*(i-1)<n:
        if interval*i>=n:
            inL.append((interval*(i-1)+1, n))
            break 
        inL.append((interval*(i-1)+1, interval*i))
        i += 1
    return inL
def f_A(inL, x, AL):
    for i in range(len(inL)):
        if x >= inL[i][0] and x <= inL[i][1]:
            p = i
            break
    if not(AL[p] >= inL[p][0] and AL[p] <= inL[p][1]):
        AL[p] = x
        return (True, AL)
    return (False, None)
'''
def f_B(x, BL):
    p0 = 0
    for i in range(1, len(BL)):
        if BL[i] < BL[i-1]:
            p0 = i
            if p0 - 2 < 0:
                p0 = 2
            for j in range(3):
                subL = [BL[p0-2], BL[p0-1], BL[p0]]
                sL = subL[:]
                sL[j] = x
                if sL == sorted(sL):
                    BL[p0-2+j] = x
                    return (True, BL)
    return (False, None)
'''
def f_B(x, BL):
  i = 1
  while BL[i] > BL[i-1] and i < len(BL)-1:
    i = i + 1
  #print(i)
  for j in range(i,len(BL)):
    if j > 2:
      Cut = [BL[j-2], BL[j-1], BL[j]]
    else:
      Cut = [BL[0], BL[1], BL[2]]
    #print(j,Cut)
    if Cut[0] < Cut[1] and Cut[1] < Cut[2]:
      #print('pass')
      continue
    else:
      if x < Cut[1] and Cut[1] < Cut[2]:
        BL[j-2] = x
        return (True, BL)
      elif x > Cut[0] and x < Cut[2]:
        BL[j-1] = x
        return (True, BL)
      elif x > Cut[1] and Cut[0] < Cut[1]:
        BL[j] = x
        return (True, BL)
  return (False, None)
def get_HV(L):
    cnt = 0
    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            cnt += 1
    return cnt
#---------- main ----------
s, n = list(map(int, input().split()))
L = list(map(int, input().split()))
xL = list(map(int, input().split()))
inL = interval(s, n)
print(inL)
i = 0
while xL.count(-1) != len(xL):
    if xL[i] == -1:
        continue
    x = xL[i]
    if not get_HV(L):
        break
    HV = get_HV(L)
    AL, BL = L[:], L[:]
    A = f_A(inL, x, AL)
    B = f_B(x, BL)
    AHV, BHV = 500, 500
    if A[0]:
        AHV = get_HV(A[1])
    if B[0]:
        BHV = get_HV(B[1])
    if AHV == min(AHV, BHV, HV):
        L = A[1][:]
        xL[i] = -1
    elif BHV == min(AHV, BHV, HV):
        L = B[1][:]
        xL[i] = -1
    print(A, B, AHV, BHV)
    print(L)
    i = (i + 1)%len(xL)
#end while
L = list(map(str, L))
output = ''
for c in L:
    output += c + ' '
print(output[:-1])
'''
def f_B(BL, x):
  i = 1
  while BL[i] > BL[i-1] and i < len(BL)-1:
    i = i + 1
  #print(i)
  for j in range(i,len(BL)):
    if j > 2:
      Cut = [BL[j-2], BL[j-1], BL[j]]
    else:
      Cut = [BL[0], BL[1], BL[2]]
    #print(j,Cut)
    if Cut[0] < Cut[1] and Cut[1] < Cut[2]:
      #print('pass')
      continue
    else:
      if x < Cut[1] and Cut[1] < Cut[2]:
        BL[j-2] = x
        return (True, BL)
      elif x > Cut[0] and x < Cut[2]:
        BL[j-1] = x
        return (True, BL)
      elif x > Cut[1] and Cut[0] < Cut[1]:
        BL[j] = x
        return (True, BL)
  return (False, None)
'''

            
            
    
