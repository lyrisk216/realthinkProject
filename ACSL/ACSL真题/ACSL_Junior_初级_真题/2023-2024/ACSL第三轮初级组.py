s = int(input())#输入s
n=int(input())#输入n
nL=input().split()#输入最开始摸到的牌--即rack
for i in range(len(nL)):
    nL[i]=int(nL[i])#nL里面的元素转换成int
sL=input().split()#输入pile里面的牌--称之为sL
for i in range(len(sL)):
    sL[i]=int(sL[i])#把sL里的元素转换成int
def is_ok(lst):#判定是否是上升序列函数
    for i in range(1,len(lst)):
        if lst[i]<=lst[i-1]:
            return False
    return True
cnt = 0#计分器初始值：如果到最后都不是上升序列就直接输出0
if is_ok(nL):#特殊判定：一开始就是上升序列的情况
    for m in nL:
        cnt += m#计算得分
else:
    while len(sL):#由于每个循环删除一个元素，所以可以直接这么写
        j = sL.pop(0)#取出sL中的第一个元素，并把这个元素从sL中删除
        flag = 0#判定是否已经操作过了
        for i in range(1,len(nL)):
            if nL[i]==j+1:#第一种操作：如果sL中取出的元素比牌架(即nL)上任意一个元素小一
                nL.pop(i-1)
                nL.insert(i-1,j)#替换元素
                flag = 1#已进行操作
                break
        for i in range(len(nL)-1):
            if nL[i]==j-1 and flag == 0:#第二种操作：如果sL取出的元素比牌架上的元素大一且没有进行过操作
                nL.pop(i+1)
                nL.insert(i+1,j)#替换元素
                flag = 1#已进行操作
                break
        for i in range(1, len(nL)-1):
            if flag == 0 and j<nL[i+1] and j>nL[i-1]\
            and (nL[i]>=nL[i+1] or nL[i]<=nL[i-1]):#第三种操作：(略) 且没有进行过操作
                nL.pop(i)
                nL.insert(i,j)#替换元素
                flag = 1#进行过操作
                break
        if flag == 0 and j<nL[1] and nL[0]>=nL[1]:#没有进行过操作，第四种操作：判定替换第一个元素是否合规
            nL.pop(0)
            nL.insert(0,j)#替换元素
            flag = 1#进行过操作
        if flag == 0 and j>nL[-2] and nL[-1]<=nL[-2]:#第五种操作:判定替换最后一个元素是否合规，没有进行过操作
            nL.pop(-1)
            nL.append(j)#替换元素
        #第六种操作略
        if flag:
            if is_ok(nL):#判定是否为上升序列
                for m in nL:
                    cnt += m#计算得分
                break#直接结束循环
print(cnt)#输出
