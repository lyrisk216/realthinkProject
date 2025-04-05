def decode_message(text, encoded_message):    
    sentences = text.split('  ')  #句子的集合
    decoded_message = ''  #初始化 decoded message
    encodings = encoded_message.split()  #每一个要寻找的位置的集合
    for encoding in encodings:   
        s, w, c = map(int, encoding.split('.'))  #用map从encoding中p赋值s,w,c三个变量，代表 sentence, word 和 字母在word 中的位置
        if s > len(sentences): #第一种可能出错判定 
            decoded_message += ' '  
            continue  
        sentence = sentences[s - 1]  #找到要寻找的sentence
        words = sentence.split()  #创建words 集合（注意最后一个是可能带句号的，要有特殊判定）
        if w > len(words):  #第二种可能出错特殊判定
            decoded_message += ' '  
            continue  
        word = words[w - 1]  #找到要找的word
        if c > len(word):  #第三种可能出错特殊判定
            decoded_message += ' '  
        else:  
            if word[c-1]!='.': 
                decoded_message += word[c - 1]#加字  
            else:#判定这个字母是否是句号
              decoded_message += ' '
      
    return decoded_message  #return value

text = input()#text的值
encoded_message = input()#要找的值
decoded_message = decode_message(text, encoded_message)  #进行寻找
print(decoded_message)#输出值
