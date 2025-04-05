def find_sentence(string, num): # 定义函数 在段落中找到第num个句子
    strLen = len(string) # 定义 strLen 为段落长度
    periodCnt = 0 # 搜完的句子的数量（结尾符号出现的次数）
    resStr = '' # 最终输出的句子
    for i in range(strLen): # 遍历段落中的每一个字符
        if periodCnt == (num - 1) and string[i] == ' ' and resStr == '': # 如果目标句子的第一个字符为空格
            continue
        if periodCnt == (num - 1) and \
           (string[i] == '.' or \
            string[i] == '!' or \
            string[i] == '?'): # 如果目标句子结束
            periodCnt += 1
            continue
        if periodCnt == (num - 1): # 如果字符在目标句子中
            resStr += string[i] # 添加该字符
        if string[i] == '.' or \
           string[i] == '?' or \
           string[i] == '!': #如果一个句子结束
            periodCnt += 1
    if resStr == '': # 如果没有找到目标句子
        return -114 # 返回 -114
    return resStr # 若找到，返回该句子

def find_word(string, num): #定义函数 在句子中找到第num个词语
    sentLen = len(string) # 定义 sentLen 为句子长度
    spaceCnt, spaceFlag = 0, 0 # 符号数量，符号判定 初始化
    word = '' # 最终输出的词语
    for i in range(sentLen): # 遍历句子中的每一个字符
        if not ((string[i] >= 'a' and string[i] <= 'z') or \
                (string[i] >= 'A' and string[i] <= 'Z') or \
                (string[i] >= '0' and string[i] <= '9')): # 如果非字母或数字
            if spaceFlag == 0: # 如果前面的字符不是符号
                spaceFlag = 1 # 下一个字符的前一个字符（这一个字符）为符号
                spaceCnt += 1 # 符号数量 + 1
        else:
            spaceFlag = 0 # 下一个字符的前一个字符（这一个字符）不为符号
            if spaceCnt == (num - 1): # 如果字符在目标词语中
                word += string[i] # 添加该字符
    if word == '': # 如果没有找到目标词语
        return -114 # 返回 -114
    return word # 若找到，返回该词语

def find_character(word, num): # 定义函数 在单词中找到第num个字符
    wordLen = len(word) # 获取单词长度
    if num > wordLen: # 如果 num 超过单词长度
        return -114 # 返回 -114
    char = word[num - 1] # 目标字符为字符串word的第num个字符（下标num - 1）
    return char # 返回该字符

def decode(bit): # 定义函数 将一个输入数据处理成三个分开的数据
    bitLen = len(bit) # 获取数据长度
    pdList = [] # 装 . 的数据库
    for i in range(bitLen): # 遍历每个字符
        if bit[i] == '.': # 如果该字符为句号
            pdList.append(i) # 添加该字符下标
    m = eval(bit[:pdList[0]]) # 获取第一个数字
    n = eval(bit[(pdList[0] + 1):pdList[1]]) # 获取第二个数字
    p = eval(bit[(pdList[1] + 1):]) # 获取第三个数字
    return m, n, p # 返回这三个数字

# ----- main ----- 主程序
text = input() # 输入段落
bitList = input().split() # 输入编号数据
newList = [] # 创建数据库（装编号数据）
result = '' # 最终的字符串
for i in range(len(bitList)): # 将编号数据存入数据库中
    m, n, p = decode(bitList[i])
    newList.append([m, n, p])
for i in range(len(bitList)): # 遍历数据库中的每一组编号数据
    sentence = find_sentence(text, newList[i][0]) # 找到目标句子
    if sentence == -114: # 如果未找到
        result += ' ' # 添加空格
        continue
    word = find_word(sentence, newList[i][1]) # 找到目标词语
    if word == -114: # 同理
        result += ' '
        continue
    char = find_character(word, newList[i][2]) # 找到目标字符
    if char == -114: # 同理
        result += ' '
        continue
    result += char # 添加最终的字符
print(result) # 输出字符串
