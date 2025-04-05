#Guess number 1~100
bottom, top = 1, 101
while bottom !=top:
    a = int((bottom + top) / 2)
    print('I guess', a)
    ans = input('> or <  ')
    if ans == '>':#move top down
        top = a
    elif ans =='<': #mpve bottom up
        bottom = a
    else:
        print('Got it')
        break
    if top - bottom ==  2:
        print('The number is ', bottom + 1)
        break
    if top - bottom == 1:
        print('error....')
        break
  


