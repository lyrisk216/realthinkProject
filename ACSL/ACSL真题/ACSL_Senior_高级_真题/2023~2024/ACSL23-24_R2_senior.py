import re

oList =[]
for i in range(62):
    oList.append([])
#一个用来储存所有字位置的list(每个的格式就是（sentence,word,character））存储顺序为小写26个，大写26个，数字10个（26+25+10 = 62）

text = input()
sentences = re.split(r'[!.?]\s*', text)[:-1]
#将一个sentence根据标点分段（!.?）

words = []
for i in range(len(sentences)):
    words.append([])
#创造一个wordlist 来将sentence分解
cnt = 0
for l in range(len(sentences)):
    c = '' #暂时的word
    for w in sentences[l]:
        if 'a'<=w<='z' or 'A'<=w<='Z' or '0'<=w<='9':
            c+=w #如果是数字，字母就加入临时word
        elif c != '':#如果不是而且word有东西（防止两个连续标点）那就把word加进wordlist
            words[l].append(c)
            c = ''
    if c != '':#把最后的word加进wordlist
        words[l].append(c)
#大丰收，根据之前的分类把每一个字符归入该有的地方
for z in range(len(words)):
    for y in range(len(words[z])):
        for x in range(len(words[z][y])):
            #下面分情况处理直接按输出方式村
            if 'a'<=words[z][y][x]<='z':
                oList[ord(words[z][y][x])-ord('a')].append((z+1,y+1,x+1))
            elif 'A'<=words[z][y][x]<='Z':
                oList[ord(words[z][y][x])-ord('A')+26].append((z+1,y+1,x+1))
            else:
                oList[int(words[z][y][x]) + 52].append((z + 1, y + 1, x + 1))
def check_out(w,n):#二分函数
    while len(oList[w])<n:
        n = n//2
    return str(oList[w][n-1][0])+'.'+str(oList[w][n-1][1])+'.'+str(oList[w][n-1][2])
txt = input()
output = '0'#(整个的输出模块，开始为0是为了后面的查最后一位模块不出错）
i = 1
for idk in range(len(txt)):
    t = txt[idk]
    if 'a' <= t <= 'z':
        if'a'<=output[-1]<='z' or 'A'<=output[-1]<='Z' or '0'<=output[-1]<='9':
            # (这行是用来检测上一个上一个输出是不是字母或数字，如果不是用空格。这个机制是因为程序可能有其他的分割符，所以要在下一次输入前检查）
            output += ' '
        output += check_out(ord(t) - ord('a'),i)
        i+=1

    elif 'A' <= t <= 'Z':
        if'a'<=output[-1]<='z' or 'A'<=output[-1]<='Z' or '0'<=output[-1]<='9':
            output += ' '
        output += check_out(ord(t) - ord('A') + 26,i)
        i+=1

    elif '0'<= t <='9':
        if'a'<=output[-1]<='z' or 'A'<=output[-1]<='Z' or '0'<=output[-1]<='9':
            output += ' '
        output += check_out(int(t) + 52,i)
        i+=1

    elif t == ' ':#这块儿偷懒喽，理论上是空格一共只应该输出了一个，但我这里只检测一次
        if output[-1]!='_':
            output+='_'

    else:
        output+=t
print(output[2:])
#最后输出去掉开头的0


#总结：其实录入是可以一次做完的，但是真的太耗费脑力了，到时候报错了没必要。有很多可以优化简化的地方，但有些问题真的是不运行不知道，只能打补丁（ps:打补丁可能占据考试的大部分时间）
